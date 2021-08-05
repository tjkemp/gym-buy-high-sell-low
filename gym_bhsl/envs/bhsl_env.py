"""A simple stock market simulator as an OpenAI gym environment."""
from collections import deque
from enum import Enum
from typing import Tuple

import gym
from gym import error, spaces

from gym_bhsl.math.average import right_average
from gym_bhsl.math.noise import OUNoise


class Action(Enum):
    HOLD = 0
    BUY = 1
    SELL = 2


class BuyHighSellLowError(Exception):
    pass


class BuyHighSellLow(gym.Env):

    metadata = {"render.modes": ["human"]}

    def __init__(
        self,
        mean: float = 10.0,
        decay: float = 0.05,
        volatility: float = 0.5,
        fee: float = 0.0,
    ):
        """The main class implementing a stock market simulator.

        The main API methods that users of this class need to know are:
        step, reset, render, close, seed

        And set the following attributes:
        action_space: The Space object corresponding to valid actions.
        observation_space: The Space object corresponding to valid observations.
        reward_range: A tuple corresponding to the min and max possible rewards.

        Args:
            mean: the mean of the stock market.
            decay: the decay rate of market shocks reverting to the mean.
            volatility: volatility of the stock market.
            fee: the transaction fee.

        """
        super().__init__()

        self.observation_space = spaces.Tuple(
            (
                spaces.Box(low=0.0, high=100.0, shape=(1,)),
                spaces.Box(low=0.0, high=100.0, shape=(90,)),
            )
        )
        self.action_space = spaces.Discrete(3)

        self._mu, self._theta, self._sigma = mean, decay, volatility
        self._noise = OUNoise(self._mu, self._theta, self._sigma)
        self._fee = fee

        self.reset()

    def reset(self) -> Tuple:
        """Reset to initial state and returns an observation."""

        self._noise.reset()
        self._stock_prices = deque([self._noise.sample() for _ in range(90)], maxlen=90)
        self._bought_at = None
        self._prev_reward = 0.0
        self._timestep = 0

        return self._state()

    def step(self, action: int):
        """Run one timestep of the environment's dynamics.

        Accepts an action and returns a tuple (observation, reward, done, info).

        Returns:
            observation (object): agent's observation of the current
                environment.
            reward (float) : amount of reward returned after previous
                action.
            done (bool): whether the episode has ended, in which case
                further step() calls will return undefined results.
            info (dict): contains auxiliary diagnostic information
                (helpful for debugging, and sometimes learning).

        """

        if not self.action_space.contains(action):
            raise BuyHighSellLowError(
                f"Invalid Action, step() received action: {action}"
            )

        self._timestep += 1
        current_price = max(self._noise.sample(), 0)
        self._stock_prices.append(current_price)

        reward = 0.0
        if action == Action.BUY.value and self._bought_at is None:
            reward = self._fee
            self._bought_at = current_price
        elif action == Action.SELL.value and self._bought_at is not None:
            reward = self._calculate_reward(current_price, self._bought_at, self._fee)
            self._bought_at = None

        self._prev_reward = reward
        return self._state()

    def render(self, mode: str = "human") -> None:
        """Render to the current terminal and return nothing."""

        if mode != "human":
            raise error.UnsupportedMode()

        texts = []
        texts.append(f"{self._timestep}.")
        texts.append(
            f"90d avg: {right_average(self._stock_prices, 90):.3f} "
            f"30d avg: {right_average(self._stock_prices, 30):.3f} "
            f"7d avg: {right_average(self._stock_prices, 7):.3f} "
        )
        if self._bought_at is not None:
            texts.append(f"Bought at {self._bought_at:.3f}.")
        elif self._prev_reward != 0.0:
            texts.append(f"Sold with profit of {self._prev_reward:.3f}.")
        else:
            texts.append("No stocks.")
        texts.append(f"Current price {self._stock_prices[-1]:.3f}.")
        print(" ".join(texts))

    def seed(self, value) -> int:
        """Set seed for reproducible randomness."""
        self._noise.seed(value)
        return value

    def _state(self) -> Tuple:
        """Return the state tuple."""

        if self._bought_at:
            bought_at = self._bought_at
        else:
            bought_at = 0.0
        state = ([bought_at], list(self._stock_prices))
        if not self.observation_space.contains(state):
            raise BuyHighSellLowError(
                "The state is not within the observations space, "
                "try adjusting noise hyperparameters"
            )
        return (state, self._prev_reward, False, {})

    def _calculate_reward(
        self, new_price: float, old_price: float, fee: float = 0.0
    ) -> float:
        """Calculate the reward for selling stocks.

        The reward is the percentage of change minus a fee.
        """
        return (new_price - old_price) / old_price - fee
