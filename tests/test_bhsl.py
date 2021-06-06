import pytest  # noqa:F401

from gym_bhsl.envs import Action, BuyHighSellLow, BuyHighSellLowError


def test_env_creation():
    env = BuyHighSellLow()
    assert isinstance(env, BuyHighSellLow)


def test_all_step_are_accepted():
    env = BuyHighSellLow()
    for action in list(Action):
        _ = env.step(action.value)


def test_nonexisting_action_raises_exception():
    env = BuyHighSellLow()
    nonexisting_action = -1
    with pytest.raises(BuyHighSellLowError):
        _ = env.step(nonexisting_action)


def test_reset_returns_state():
    env = BuyHighSellLow()
    state, reward, done, info = env.reset()
    assert env.observation_space.contains(state)
    reward_low, reward_high = env.reward_range
    assert reward_low <= reward <= reward_high
    assert isinstance(done, bool)
    assert isinstance(info, dict)


def test_render_is_implemented():
    env = BuyHighSellLow()
    env.render()


def test_close_is_implemented():
    env = BuyHighSellLow()
    env.close()


def test_seed():
    env = BuyHighSellLow()
    env.seed(50)
