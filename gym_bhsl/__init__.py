from gym.envs.registration import register

__VERSION__ = "0.1.0"

register(
    id="buy-high-sell-low-v0",
    entry_point="gym_bhsl.envs:BuyHighSellLow",
)
