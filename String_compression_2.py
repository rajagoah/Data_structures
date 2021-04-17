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
        self.strng = input
        self.lst = list()
        self.counter = 1
        self.target_str = None

    def compressor(self):
        #storing in list
        self.lst = list(self.strng)
        print(self.lst)

        #edge case 1
        if len(self.strng) == 0:
            return 0

        #edge case 2
        if len(self.strng) == 1:
            return self.lst[0] + str(1)

        #driver logic
        i = 0
        while i < len(self.lst):

            if self.lst[i] == self.lst[i-1]:
                self.counter += 1
                #self.target_str = self.lst[i]+ str(self.counter)
                self.lst[i] = self.lst[i]+ str(self.counter)
                i += 1
            else:
                #self.target_str = self.lst[i]+ str(self.counter)
                self.lst[i] = self.lst[i]+ str(self.counter)
                self.counter = 1
                i += 1
        return ''.join(self.lst)

if __name__ == "__main__":
    #a = 'aabbcc'
    #a = 'ab'
    a = 'a'

    d = String_compression(a).compressor()
    print(d)

