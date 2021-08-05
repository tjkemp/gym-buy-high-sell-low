# Gym Buy High Sell Low

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gym-buy-high-sell-low)
![License](https://img.shields.io/github/license/tjkemp/gym-buy-high-sell-low)
![GitHub last commit](https://img.shields.io/github/last-commit/tjkemp/gym-buy-high-sell-low)

*Gym Buy High Sell Low is* an OpenAI Gym simulated stock market environment that allows training agents to do favorable trades on a hypothetical stock market. Please, don't use this for serious purposes. The goal for this project is personal learning. I feel trying to beat the stock market is a rite of passage when you're getting into reinforcement learning.

Obviously, "buy high, sell low" is an attempt at humour and obviously a horrible way to do trading.

## Prerequisites

- Python >= 3.7 (tested with latest 3.7, 3.8 and 3.9)

## Getting started

Install the package either from Pypi or from the repository.

```bash
pip istall gym-buy-high-sell-low
```

To install from the repository, follow these steps:

Linux and macOS:

```bash
git clone https://github.com/tjkemp/gym-buy-high-sell-low

# create and enter a Python environment here before proceeding

pip install requirements/requirements.txt
pip install -e .
```

After installing the package to create an instance of the environment first import both `gym_bhsl` and OpenAI's `gym` package:

```
>>> import gym_bhsl
>>> import gym
>>> env = gym.make('BuyHighSellLow-v0')
```

The environment instance implements the usual OpenAI Gym environment methods.

To see the observation space and the action space of the environment, use the `env.observation_space` and `env.action_space` properties:

```
>>> env.observation_space
Tuple(Box(0.0, 100.0, (1,), float32), Box(0.0, 100.0, (90,), float32))

>>> env.action_space
Discrete(3)
```

The observation space is a tuple of two `Box` objects, one for the price of the bought stock (or `0.0` if no stock is owned. The second object is the price history for the last 90 days (timesteps).

The action space is a discrete space of size 3. Integer `0` means hold/wait, `1` means buy, `2` means sell.

`render()` prints out the current state of the environment in a simplified human readable format.

```
> env.reset()
> env.render()
0. 90d avg: 9.224 7d avg: 8.857. No stocks. Current price 8.192.
> env.action(1); env.render()  # Buy stocks
1. 90d avg: 9.212 7d avg: 8.742. Bought at 8.802. Current price 8.946.
> env.action(0); env.render()  # Hold
2. 90d avg: 9.185 7d avg: 8.684. Bought at 8.802. Current price 9.918.
> env.action(2); env.render()  # Sell stocks
3. 90d avg: 9.185 7d avg: 8.684. Sold with a profit of 0.166 %. Current price 10.264.
```

The reward is the profit/loss made from the last trade in percentage. Sell actions are executed on the next timesteps price. You can only buy and hold one stock at a time.

## The simulation

The stock market is simulated as an Ornstein-Uhlenbeck process. The process is a random walk with a constant mean and a constant standard deviation. At the start of a task the process is initialized with 90 timesteps of random stock price and the price is updated after each timestep.

## Author

* tjkemp
