"""
Using this class to practice the use of PRIVATE method called __len__
"""
class dynarray():

    def __init__(self):
        self.n = 0 #number of elements in array
        self.size = 1 #the capacity of the array
        self.array = [1,2,3,4,5]

    def __len__(self):
        return len(self.array)

    def print_length(self):
        leng = self.__len__()
        print(f" {leng} is the number of elements in the array".format(leng))


if __name__ == "__main__":
    d = dynarray()
    d.print_length()

