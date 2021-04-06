"""
calling the PRIVATE method __get_item__()  interanlly, to calculate the product
"""
class dynarray():

    def __init__(self):
        self.n = 0 #number of elements in array
        self.size = 1
        self.array = [1,2,3,4]

    def __get_item__(self,element):
        return self.array[element]

    def multiply(self, multiple):
        val = self.__get_item__(1)
        return val*multiple

if __name__ == "__main__":
    d = dynarray()
    result = d.multiply(3)
    print(f"{result} is the output".format(result))