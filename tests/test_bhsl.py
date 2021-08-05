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


def test_setting_seed_creates_reprocubility():
    env = BuyHighSellLow()
    env.seed(50)
    env.reset()
    state, _, _, _ = env.step(0)

    env.seed(50)
    env.reset()
    state_new_task, _, _, _ = env.step(0)

    assert state[1] == state_new_task[1]


def test_reward_calculation():
    env = BuyHighSellLow()
    new_price, old_price = 10.0, 9.0
    expected_reward = 0.1111

    reward = env._calculate_reward(new_price, old_price)

    assert reward == pytest.approx(expected_reward, 0.001)


def test_reward_calculation_with_fee():
    env = BuyHighSellLow()
    new_price, old_price, fee = 15.0, 10.0, 0.1
    expected_reward = 0.4

    reward = env._calculate_reward(new_price, old_price, fee)

    assert reward == pytest.approx(expected_reward, 0.01)
