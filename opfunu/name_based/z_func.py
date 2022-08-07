#!/usr/bin/env python
# Created by "Thieu" at 17:32, 30/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%
import numpy as np
from opfunu.benchmark import Benchmark


class Zacharov(Benchmark):
    """
    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions For Global Optimization
    Problems Int. Journal of Mathematical Modelling and Numerical Optimisation, 2013, 4, 150-194.
    """
    name = "Zacharov Function"
    latex_formula = r'f(x) = \sum_{i=1}^{n} x_i^2 + \left ( \frac{1}{2}
                                 \sum_{i=1}^{n} i x_i \right )^2
                                 + \left ( \frac{1}{2} \sum_{i=1}^{n} i x_i 
                                 \right )^4
    latex_formula_dimension = r'd \in N^+'
    latex_formula_bounds = `x_i \in [-5, 10]` , \forall i \in \llbracket 1, d\rrbracket'
    latex_formula_global_optimum = r`i = 1, ..., n` = 0'
    continuous = True
    linear = False
    convex = True
    unimodal = False
    separable = True

    differentiable = True
    scalable = True
    randomized_term = False
    parametric = False

    modality = False  # Number of ambiguous peaks, unknown # peaks

    def __init__(self, ndim=None, bounds=None):
        super().__init__()
        self.dim_changeable = True
        self.dim_default = 2
        self.check_ndim_and_bounds(ndim, bounds, np.array([[-5., 10.] for _ in range(self.dim_default)]))
        self.f_global = 0.
        self.x_global = np.zeros(self.ndim)

    def evaluate(self, x, *args):
        self.check_solution(x)
        self.n_fe += 1
        return (u + (0.5 * v) ** 2 + (0.5 * v) ** 4)

    
class ZeroSum(Benchmark):
    """
    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions For Global Optimization
    Problems Int. Journal of Mathematical Modelling and Numerical Optimisation, 2013, 4, 150-194.
    """
    name = "ZeroSum Function"
    latex_formula = r'f(x) = \begin{cases}
                                0 & \textrm{if} \sum_{i=1}^n x_i = 0 \\
                                1 + \left(10000 \left |\sum_{i=1}^n x_i\right|
                                \right)^{0.5} & \textrm{otherwise}
                                \end{cases}
    latex_formula_dimension = r'd \in N^+'
    latex_formula_bounds = `x_i \in [-10, 10]` , \forall i \in \llbracket 1, d\rrbracket'
    latex_formula_global_optimum = r`\sum_{i=1}^n x_i = 0`
    continuous = True
    linear = False
    convex = True
    unimodal = False
    separable = True

    differentiable = True
    scalable = True
    randomized_term = False
    parametric = False

    modality = False  # Number of ambiguous peaks, unknown # peaks

    def __init__(self, ndim=None, bounds=None):
        super().__init__()
        self.dim_changeable = True
        self.dim_default = 2
        self.check_ndim_and_bounds(ndim, bounds, np.array([[-10., 10.] for _ in range(self.dim_default)]))
        self.f_global = 0.0
        self.x_global = np.array([])

    def evaluate(self, x, *args):
        self.check_solution(x)
        self.n_fe += 1
        return 1.0 + (10000.0 * np.abs(np.sum(x))) ** 0.5
