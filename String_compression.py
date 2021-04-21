"""
1. parse through the input array and then count the occurrences of letters
2. Append the letters with counter value
3. After parsing through the input string, parse through the elements in the dictionary
4. combine the key+value to get the output like A3 or b2.
5. Append this value to a list
6. Finally convert the list to a string and return to the calling object
7. This code doesn't handle the input such as 'AaBBaB' which should output A1a1B2a1B1. The output per the below code
will be A1a2B3 which is incorrect
"""
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
    a = 'AaBbbbB'
    d = String_Compression(a).compressor()
    print(d)




