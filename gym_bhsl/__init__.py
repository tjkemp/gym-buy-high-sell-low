from gym.envs.registration import register

register(
    id="buy-high-sell-low-v0",
    entry_point="gym_bhsl.envs:BuyHighSellLow",
)
