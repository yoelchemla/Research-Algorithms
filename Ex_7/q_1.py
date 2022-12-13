import numpy as np
import cvxpy as cp
import time
import random
import matplotlib.pyplot as plt

next_time = 0


def my_timer(orig_func):
    def wrapper(*args, **kwargs):
        global next_time
        next_time = 0
        time_prev = time.time()
        result = orig_func(*args, **kwargs)
        next_time = time.time() - time_prev
        print(f'my_timer: {orig_func.__name__} run in: {next_time - time_prev} sec')
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
def cvxpy_solve(x, obj, constraints):
    """
    :param(1) x: variables
    :param(2) obj: sum of A@y-B matrix
    :param(3) constraints:
    :return: answer of the problem
    """
    prob = cp.Problem(obj, constraints)
    prob.solve()
    return x.value


numpy_test = {}
cvxpy_test = {}


def generate_random_linear_equation(i):
    global next_time
    global numpy_test
    global cvxpy_test
    print("matrix from rank", i)
    m = n = i
    A = np.random.randint(-10, 10, (m, n))  # random numbers for the Matrix A in this range
    B = np.random.randint(-100, 100, m)  # random numbers for the Vector B in this range
    print(f"Matrix A {m}x{n} is: \n {A} \n, Matrix B is : \n {B} \n")
    print("the solution of numpy is: ", solve_by_numpy(A, B))
    numpy_test[m] = next_time
    x = cp.Variable(n)
    constraints = [A @ x == B]
    obj = cp.Minimize(cp.sum(A @ x - B))  # calculate the sum of this linear equation
    cvxpy_test[m] = next_time
    print("the solution of cvxpy is: ", cvxpy_solve(x, obj, constraints))
    print("\n")


if __name__ == '__main__':
    value1 = input("Please enter the minimum rank of the matrix :\n")
    value2 = input("Please enter the maximum rank of the matrix :\n")

    # make sure that the input is an integer
    min_rank = int(value1)
    max_rank = int(value2)

    for i in range(min_rank, max_rank):
        generate_random_linear_equation(i)
