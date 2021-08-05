import numpy as np


class OUNoise:
    """Ornstein-Uhlenbeck process."""

    def __init__(self, mu: float = 0.0, theta: float = 0.15, sigma: float = 0.2):
        """Initialize the process.

        Args:
            mu: the equilibrium (the mean of the gaussian noise).
            theta: the decay rate of the noise (the amount of randomness regard to
                previous sample).
            sigma: the volatility, values will be roughly [-6*sigma, 6*sigma].

        """
        self.mu = mu
        self.theta = theta
        self.sigma = sigma
        self.reset()

    def seed(self, seed: int) -> None:
        """Set seed for reproducible randomness.

        Note that `numpy.random.seed` is not thread-safe.
        """
        np.random.seed(seed)

    def reset(self) -> None:
        """Reset the internal state to mean (mu)."""
        self.state = self.mu

    def sample(self) -> float:
        """Update internal state and return it as a sample."""
        x = self.state
        dx = self.theta * (self.mu - x) + self.sigma * np.random.randn()
        self.state = x + dx
        return self.state
