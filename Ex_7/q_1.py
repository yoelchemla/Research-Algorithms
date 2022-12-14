import time
import numpy as np
import cvxpy as cp
import random

from matplotlib import pyplot as plt

next_time = 0


# credit: https://dev.to/kcdchennai/python-decorator-to-measure-execution-time-54hk
def timer(origin_function):
    def wrapper(*args, **kwargs):
        global next_time
        next_time = 0
        time_prev = time.time()
        answer = origin_function(*args, **kwargs)
        next_time = time.time() - time_prev  # the different
        print(f'timer: {origin_function.__name__} run in: {next_time} second')
        return answer

    return wrapper


# credit: https://github.com/erelsgl-at-ariel/research-5783/blob/main/07-python-numstack/code/1.numpy.ipynb
# this function calculate the solution by numppy library
@timer
def solve_by_numpy(A, B):
    """
     return: solve of matrix A*x=B
    """
    return np.linalg.solve(A, B)


# this function calculate the solution by cvxpy library
# credit: https://github.com/erelsgl-at-ariel/research-5783/blob/main/07-python-numstack/code/6.cvxpy.ipynb
@timer
def cvxpy_solve(x, obj, con):
    """
    obj = sum of A@x-B matrix
    return: answer of the problem
    """
    prob = cp.Problem(obj, con)
    prob.solve()
    return x.value


numpy_test = {}
cvxpy_test = {}


def generate_random_linear_equation(i):
    global numpy_test
    global cvxpy_test
    global next_time

    print("matrix from rank", i)
    m = n = i

    """
    numpy solution
    """
    # init the parameters
    A = np.random.randint(-10, 10, (m, n))  # random numbers for the Matrix A in this range
    B = np.random.randint(-100, 100, m)  # random numbers for the Vector B in this range
    print(f"Matrix A {m}x{n} is: \n {A} \n")
    print(f"Matrix B is : \n {B} \n")
    print("the solution of numpy is: ", solve_by_numpy(A, B))
    numpy_test[m] = next_time

    """
    cvxpy solution
    """
    # init the parameters
    x = cp.Variable(n)  # first parameter
    con = [A @ x == B]  # second parameter
    obj = cp.Minimize(cp.sum(A @ x - B))  # third parameter, calculate the sum of this linear equation
    cvxpy_test[m] = next_time
    print("the solution of cvxpy is: ", cvxpy_solve(x, obj, con))
    print("\n")


# credit: https://github.com/erelsgl-at-ariel/research-5783/blob/main/07-python-numstack/code/2.matplotlib.ipynb
def print_diagram():
    global cvxpy_test
    global numpy_test

    plt.plot(numpy_test.keys(), numpy_test.values(), color='blue')
    plt.plot(cvxpy_test.keys(), cvxpy_test.values(), color='green')
    plt.show()
    plt.show()


if __name__ == '__main__':
    # the user will choose the ranks of matrix
    value1 = input("Please enter the minimum rank of the matrix :\n")
    value2 = input("Please enter the maximum rank of the matrix :\n")

    # make sure that the input is an integer
    min_rank = int(value1)
    max_rank = int(value2)

    for i in range(min_rank, max_rank):
        generate_random_linear_equation(i)
    print_diagram()
