import ctypes
class DynamicArray_test():

    def __init__(self, arr):
        self.arr = arr
        self.n = 0 #this var will be used in a method below
        self.capacity = 1 #this

    def len(self):
        n = len(self.arr)
        return print(' The number of elements in the array is: ', n)

    def resize(self, new_capacity):
        """
        Resize the existing array by creating a new array of greater size and assigning the new one to the old one
        :param new_capacity:
        :return:
        """
        B = self.make_array(new_capacity)

        #reference all existing values to the 'B' array
        for element in range(self.n):
            B[element] = self.arr[element]

        #call ARR the new bigger array
        self.arr = self.B

        #reset the capacity
        self.capacity = new_capacity

    def append(self, element):
        """
        add element to the end of an array
        :param element:
        :return:
        """
        self.arr[self.n] = element

        #set the self.n value to the index of the newly added element
        self.n += 1

    def make_array(self, new_capacity):
        """
        returns a new array with capacity = New capacity
        This is needed to be able to extend the capacity of the existing array
        :param new_capacity:
        :return:
        """
        return (new_capacity * ctypes.py_object)()


if __name__=="__main__":
    arr = [1,2,3,4,5,5,6,66,90]
    l = DynamicArray_test(arr)
    l.len()

    print(len(l.make_array(10)))
    print("done")