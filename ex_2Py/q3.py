class List(list):

    # constructor
    def __init__(self, *args):
        self.array = []
        if len(args) < 1:
            return
        for i in args:
            if not isinstance(i, list):
                raise Exception("The types do not match")
            self.array.append(i)

    def __getitem__(self, *args):
        if len(args) < 1:
            return
        else:
            if isinstance(args[0], int):
                return self.array[args[0]]
            else:
                x = list(args[0])

            ans = self.array[x[0]]
            for i in x[1:]:
                ans = ans[i]
            return ans

    def __str__(self):
        return str(self.array)

    def append(self, *args):
        """
        add element
        """
        if len(args) < 1:
            return
        for i in args:
            if not isinstance(i, list):
                raise Exception("The types do not match")
            self.array.append(i)

    def remove(self, number: int) -> None:
        """
        delete element
        """
        return self.array.pop(number)


if __name__ == '__main__':

    example_list = List(
        [[1, 2, 3, 33], [4, 5, 6, 66]],
        [[7, 8, 9, 99], [10, 11, 12, 122]],
        [[13, 14, 15, 155], [16, 17, 18, 188]],
    )

    print( "1. the result of append  [[[1, 2, 3, 33], [4, 5, 6, 66]], [[7, 8, 9, 99], [10, 11, 12, 122]],"
        " [[13, 14, 15, 155], [16, 17, 18, 188]], [1, 2, 3]] -----> \n", example_list)
    print("2. the result is  ---->  ", example_list[0, 1, 3]) #66

    print("line 0, array, index 3: ", example_list[0, 0, 3])

    print("the first array in the first line is: ", example_list[0, 0])
    print("the line 2 is: ", example_list[[2]])
    print("the line 0 is: ", example_list[0])

    print()
    print()


    a = List(["Y", "o", "e", "l"], ["C", "h", "e", "m", "l", "a"], ["L", "i", "s", "t"])

    print(a)
    a.append([0, 1, 2, 3])
    print(a)

    a.remove(2) #delete the place 2
    print(a)
    a.append(['s', 't', 'u', 'd', 'e', 'n', 't'])
    print(a)

    a.remove(2)
    print(a) #[['Y', 'o', 'e', 'l'], ['C', 'h', 'e', 'm', 'l', 'a'], ['s', 't', 'u', 'd', 'e', 'n', 't']]