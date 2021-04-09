class dyn_array():

    def __init__(self):
        self.n = 0 #num of elements in the array
        self.capacity = 1 #the size of the array
        self.A = [None]

    def __getitem__(self, index):
        return self.A[index]

    def __resize__(self, new_capacity):
        B = [None] * new_capacity

        for k in range(len(self.A)):
            B[k] = self.A[k]
        self.A = B
        return self.A

    def __setitem__(self, index):
        if self.n == self.capacity:
            self.A = self.__resize__()





