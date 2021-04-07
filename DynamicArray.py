class DynamicArray():

    def __init__(self):
        self.n = 0 #declare a var to store the number of elements in the array
        self.capacity = 1 #declare a var to store the max size of the array. This will be defaulted to 1
        self.A = [None] #declare an array with None as the 1st element. Len(A)=1 but A[0] = None

    def __resize__(self, new_capacity):
        B = [None] #declare another None list that will be used to extend the existing array
        B = B * new_capacity #resizing the B array to double the length of existin array A

        for k in range(len(self.A)):
            B[k] = self.A[k] #assigning all elements in existing array A to expanded array B
        self.A = B
        self.capacity = len(self.A)
        return self.A

    def append(self, element):
        if self.n == self.capacity:
            self.A = self.__resize__(2*len(self.A))

        self.A[self.n] = element
        self.n += 1
        print(self.A)

if __name__ == "__main__":
    d = DynamicArray()
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    d.append(5)







