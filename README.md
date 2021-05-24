# Gym Buy High Sell Low

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/gym-buy-high-sell-low)
![License](https://img.shields.io/github/license/tjkemp/gym-buy-high-sell-low)
![GitHub last commit](https://img.shields.io/github/last-commit/tjkemp/gym-buy-high-sell-low)

Gym Buy High Sell Low is an OpenAI Gym simulated stock market environment that allows using it to train agents to do favorable trades. Please, don't use this for serious purposes. The goal for this project is personal learning.

Obviously, "buy high, sell low" is an attempt at sarcastic humour and would be a horrible way to do trading.

## Prerequisites

- Python 3.9 (probably works with earlier versions)

## Getting started

To install, follow these steps (mind usage of Python environments):

Linux and macOS:
```bash
git clone https://github.com/tjkemp/gym-buy-high-sell-low
# create and enter a Python environment here before proceding
pip install requirements/requirements.txt
pip install -e .
```

To use the project, follow these steps:

```
> import gym
> import gym_bhsl
> env = gym.make('gym-buy-high-sell-low-v0')
> env.reset()
> env.render()
0. 90d avg: 9.224 7d avg: 8.857. No stocks. Current price 8.192.
> env.action(1); env.render()  # Buy stocks
1. 90d avg: 9.212 7d avg: 8.742. Bought at 8.802. Current price 8.946.
> env.action(0); env.render()  # Hold
2. 90d avg: 9.185 7d avg: 8.684. Bought at 8.802. Current price 9.918.
> env.action(2); env.render()  # Sell stocks
3. 90d avg: 9.185 7d avg: 8.684. Sold with profit of 1.462. Current price 10.264.
```

## Author

* tjkemp
