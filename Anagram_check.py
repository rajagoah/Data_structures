class anagramchecker(object):
    def __init__(self):
        pass #initializing with an empty contructor

    def __len__(self, str):
        return len(str) #creating this special method so that the len() can be used on the instance of this class

    def AnagramChecker(self, str):
        arr = self.__ArrayConverter__(str) #This method converts the string to an array
        return arr

    def __ArrayConverter__(self, str):
        arr = self.__placeholder_arr__(str) #breaks the strings individual letters to elements of an array
        return arr

    def __placeholder_arr__(self, str):
        s = [] #var to store the individual letters from the incoming string 'str'
        str = str.lower() #suppressing the case as per business requirements
        for i in str:
            s.append(i) #looping through each item in str and storing in a list
        s = self.__remove_spaces__(s) #sending this to a method to pop out spaces
        s.sort() #sorting the array before returning to main()
        return s

    def __remove_spaces__(self, arr):
        for i in arr:
            if i == " ":
                    arr.pop(arr.index(i)) #poping out elements if it is a space
        return arr


if __name__ == "__main__":

    #a = "public relations"
    #b = "crap built on lies"
    a = "clint eaSTwood"
    b = "old west action"

    obj = anagramchecker()
    arr1= obj.AnagramChecker(a)
    arr2= obj.AnagramChecker(b)

    if arr1 == arr2:
        print(" This is an anagram")
    else:
        print(" not an anagram")


