class String_Compression():

    def __init__(self, array):
        self.array = array #to store input strings
        self.counter = 1 #to count the number of occurrence of the letter
        self.dic = dict() #to store the mapping of occurrences to the letters
        self.strng = list() #to sotre the value such as--['A1', 'B2']

    def compressor(self):
        for i in range(len(self.array)):
            if self.array[i] not in self.dic: #validating if the element exists in the dictionary
                self.dic[self.array[i]] = self.counter #if not there then add the value of the counter
            else:
                self.dic[self.array[i]] = self.dic[self.array[i]] + 1 #if it exists then increment the value

        for k, v in self.dic.items(): #once parsed through the value in the input string, then parse through the dic items and combine them
            self.strng.append(k + str(v)) #First combine the key and value and then append the values in the dic to the list
        return ''.join(self.strng) #use the join operation to convert the list to strings

if __name__ == "__main__":
    a = 'AsSAAdytza'
    d = String_Compression(a).compressor()
    print(d)




