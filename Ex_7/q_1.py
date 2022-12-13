import numpy as np
import cvxpy as cp
import random
import matplotlib.pyplot as plt


def my_timer(orig_func: callable):
    import time

    def wrapper(*args, **kwargs):
        time_before = time.time()
        result = orig_func(*args, **kwargs)
        time_after = time.time()
        print(f'my_timer: {orig_func.__name__} ran in: {time_after-time_before} sec')
        return result
    return wrapper


# credit: https://github.com/erelsgl-at-ariel/research-5783/blob/main/07-python-numstack/code/1.numpy.ipynb
# this function calculate the solution by numppy library
@my_timer
def solve_by_numpy(A, B):
    """
     :param(1) A: matrix A
     :param(2) B:  matrix B
     :return: solve of matrix A*x=B
    """
    return np.linalg.solve(A, B)


# this function calculate the solution by cvxpy library
# credit: https://github.com/erelsgl-at-ariel/research-5783/blob/main/07-python-numstack/code/6.cvxpy.ipynb
@my_timer
def cvxpy_solve(y, obj, constraints):
    """
    :param(1) y: variables
    :param(2) obj: sum of A@y-B matrix
    :param(3) constraints:
    :return: answer of the problem
    """
    prob = cp.Problem(obj, constraints)
    prob.solve()
    return y.value
