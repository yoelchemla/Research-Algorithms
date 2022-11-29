import doctest


class bounded_subset:
    def __init__(self, lst: list, C: int):
        self.c = C
        self.lst = lst
        st = "1"  # the first permutation that invalid
        self.rep = ""  # the next permutation
        self.stop = st.ljust(len(lst) + 1, '0')
        self.rep = st.ljust(len(lst) + 1, '0')[1:]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.lst) == 0:
            raise StopIteration
        flag = True
        while flag:
            flag = False
            self.rep = bin(int(self.rep, 2) + 1)[2:]  # binary action
            binary_str = self.rep.zfill(len(self.lst))  # creating current representation (add zero until we arrive
            # to the number)
            if binary_str == self.stop:
                raise StopIteration
            temp_sum = 0
            temp_lst = []
            for i in range(len(self.lst)):  # pass on the length of the list
                if binary_str[i] != "0":
                    temp_sum = temp_sum + self.lst[i]
                    temp_lst.append(self.lst[i])
                    if temp_sum > self.c:  # if the current sum bigger than the sum
                        flag = True
                        break
            if not flag:
                return temp_lst


if __name__ == '__main__':

    for s in bounded_subset([1, 2, 3], 4):
        print(s)
    print("---")

    for s in bounded_subset([1, 2, 3], 6):
        print(s)
    print("---")

    for s in bounded_subset([0, 0, 0], 1):
        print(s)
    print("---")
