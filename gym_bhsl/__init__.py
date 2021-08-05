from gym.envs.registration import register

__VERSION__ = "0.2.1"

register(
    id="BuyHighSellLow-v0",
    entry_point="gym_bhsl.envs:BuyHighSellLow",
)
