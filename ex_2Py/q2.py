# i used by this website https://www.geeksforgeeks.org/function-wrappers-in-python/

x = None
name = None
f_of_x = None


def lastcall(func):
    def wrapper(*args, **kwargs):
        global x
        global name
        global f_of_x

        arg = args[0]

        if name is None:  # init
            x = arg
            name = func.__name__
            f_of_x = func(x)
            print(str(f_of_x))

        elif arg == x and name == func.__name__:  # exist
            print("I already told you that the answer is", str(f_of_x), "!")

        else:
            x = arg
            name = func.__name__
            f_of_x = func(x)
            print(str(f_of_x))
        return

    return wrapper


@lastcall
def sqrt(x: float):
    return x ** 0.5


@lastcall
def is_even(x: int) -> bool:
    return x % 2 == 0


@lastcall
def power(x: float):
    return x ** 2


if __name__ == '__main__':
    print()

    print("Check the sqrt func:")
    print("the sqrt of 9 is: ")
    sqrt(9)
    print()
    print(" sqrt(-1) is a complex number:")
    sqrt(-1)
    print()
    sqrt(7)
    print("the sqrt of 7 is: ")
    sqrt(7)  # duplicate

    print()

    print("Check the func_is_even:")
    print("16 is even?")
    is_even(16)
    print()
    print("5 is even?")
    is_even(5)
    print()
    print("8 is even?")
    is_even(8)
    print()
    print("7.3 is even?")
    is_even(7.3)
    print()
    print("13 is even?")
    is_even(13)
    print()
    print("13 is even?:")
    is_even(13)
