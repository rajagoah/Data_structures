import datetime

class anagramchecker(object):
    def __init__(self):
        pass #initializing an empty constructor

    def __len__(self, str):
        return len(str) #creating this special method so that the len() can be used on the instance of this class

    def AnagramChecker(self, str):
        arr = self.__ArrayConverter__(str) #This method converts the string to an array
        return arr

    def __ArrayConverter__(self, str):
        arr = self.__placeholder_arr__(str) #breaks the strings individual letters to elements of an array
        return arr

    def __placeholder_arr__(self, str):
        s = []  # var to store the individual letters from the incoming string 'str'
        s.clear()
        str = str.lower() #suppressing the case as per business requirements
        for i in str:
            if i == " ":
                pass
            else:
                s.append(i) #looping through each item in str and storing in a list
        s.sort() #sorting the array before returning to main()
        return s


if __name__ == "__main__":

    #a = "public relations"
    #b = "crap built on lies"
    #a = "clint eaSTwood"
    #b = "old west action"
    a= "TnA"
    b= "antaaaaa"


    obj = anagramchecker()
    arr1 = obj.AnagramChecker(a)
    arr2 = obj.AnagramChecker(b)

    if arr1 == arr2: #and len(arr1) == len(arr2):
        print(" This is an anagram")
    else:
        print(" not an anagram")



