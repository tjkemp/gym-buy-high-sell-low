import pytest

from gym_bhsl.math.noise import OUNoise


def test_object_creation():
    obj = OUNoise()
    assert isinstance(obj, OUNoise)


def test_object_creation_wih_params():
    mu, theta, sigma = 0.1, 0.2, 0.3
    noise = OUNoise(mu=mu, theta=theta, sigma=sigma)
    assert mu == noise.mu
    assert theta == noise.theta
    assert sigma == noise.sigma


def test_sampling():
    noise = OUNoise(mu=1.0, theta=0.01, sigma=0.01)
    sample = noise.sample()
    assert sample == pytest.approx(1.0, 0.1)


def test_randomness_is_predictable():
    noise = OUNoise()
    sample_noseed = noise.sample()
    seed = 10
    noise.seed(seed)
    noise.reset()
    sample1 = noise.sample()
    assert sample_noseed != sample1
    noise.seed(seed)
    noise.reset()
    sample2 = noise.sample()
    assert sample1 == sample2
