"""Utilities for constructing symbolic matter expressions, usually via the Stress-Energy Tensor
"""

from sympy import Array, symbols
from sympy.matrices import diag, zeros

from collapse.symbolic.metric import Metric


def vacuum(metric: Metric) -> Array:
    """Compute the stress energy tensor for a vacuum (zeros)

    Args:
        metric:
            Metric

    Returns:
        Array, the full stress energy tensor as a matrix
    """
    dim = metric.coord_system.dim
    return zeros(dim, dim)


def perfect_fluid(metric: Metric, fluid_velocity=None) -> Array:
    """Compute the stress energy tensor for a perfect fluid in a given metric

    Args:
        metric:
            Metric

    Returns:
        Array, the full stress energy tensor as a matrix
    """
    p, rho = symbols('p rho')
    dim = metric.coord_system.dim
    return (p + rho) * diag(*[1, 0, 0, 0][:dim]) + p * metric.matrix
