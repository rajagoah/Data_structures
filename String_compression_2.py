"""
a cleaner and efficient way to compress strings
1. Check for the following edge cases:
    a. len == 0
    b. len = 1
2. while loop
    a. if the current element in the list is the same as the previous element, then increment counter
    b. if not the same as the previous element, then reset counter and concatenate the count with the element
"""
class String_compression():

    def __init__(self, input):
        self.input = input
        self.counter = 1
        self.target_str = ''

    def __len__(self):
        return len(self.input)

    def compressor(self):

        #storing the leng in a variable
        leng = self.__len__()

        #storing in list
        print(self.input)

        #edge case 1
        if leng == 0:
            return 0

        #edge case 2
        if leng == 1:
            return self.input[0] + str(1)

        #driver logic
        i = 1
        while i < leng:

            if self.input[i] == self.input[i-1]:
                self.counter += 1
            else:
                self.target_str = self.target_str + self.input[i-1] + str(self.counter)
                self.counter = 1
            i += 1
        self.target_str = self.target_str + self.input[i - 1] + str(self.counter)
        return self.target_str

if __name__ == "__main__":
    #a = 'AABbcC' this passed correctly
    a = 'AAAaa'

    d = String_compression(a).compressor()
    print(d)

