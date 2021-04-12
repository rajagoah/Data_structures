class Array_sum_pair():
    def __init__(self, array):
        self.lst = array[0]
        self.result = array[1]
        self.counter = 0
        self.pointer_element = array[1]

    def ArraySumPairChecker(self):
        for k in range(len(self.lst)):
            if k != (len(self.lst) - 1):
                s = self.lst[k] + self.lst[k+1]
                if s == self.result:
                    print(f" The pair is: {self.lst[k]}, {self.lst[k+1]}".format(self.lst[k], self.lst[k+1]))
                    self.counter += 1
                else:
                    continue
        return self.counter

if __name__  == "__main__":
    a = [[1, 3, 2, 2], 4]
    print(Array_sum_pair(a).ArraySumPairChecker())

