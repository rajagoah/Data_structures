import ctypes

class DynamicArray():

    def __init__(self):
        self.n = 0 #number of elements
        self.capacity = 1 #size of the array
        self.array = [None]

    def append(self, element):
        if self.n == self.capacity:
            array_expanded = [None]*(self.capacity*2)
            #performing element level assignments
            for k in range(len(self.array)):
                array_expanded[k] = self.array[k]
            #perform list reassignment
            self.array = array_expanded
            self.capacity = len(self.array)

        self.array[self.n] = element
        self.n+=1
        return self.array

if __name__=="__main__":
    d = DynamicArray()
    arr = d.append(1)
    print(arr)

    arr = d.append(2)
    print(arr)

    arr = d.append(3)
    print(arr)

    arr = d.append(4)
    print(arr)

    arr = d.append(5)
    print(arr)

    arr = d.append(6)
    print(arr)

    arr = d.append(7)
    print(arr)

    arr = d.append(8)
    print(arr)

    arr = d.append(9)
    print(arr)