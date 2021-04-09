def AnagramChecker(str1, str2):
    str1 = str1.replace(' ', '').lower()  # replacing spaces with empty string
    str2 = str2.replace(' ', '').lower()  # replacing spaces with empty string

    # really good check edge case check. if the lengths of the 2 strings  isn't the sme then we can safely say that the strings are not anagrams
    if len(str1) != len(str2):
        return False

    d1 = {}  # declaring empty dictionaries. This will store the letter occurrences

    #adding letters from string 1 in to the empty dictionary
    for k in str1:
        # validating for d1
        if k not in d1:
            d1[k] = 1
        elif k in d1:
            d1[k] += 1

    #reducing the letters occurrence from the dictionary loaded above
    for k in str2:
        # validating for d1
        if k not in d1:
            d1[k] = 1
        elif k in d1:
            d1[k] -= 1

    #if the letters count in the dictionary is 0, then we can say that the strings are anagrams
    for k in d1:
        if d1[k] != 0:
            return False
    return True




if __name__ == "__main__":
    #str1 = input(" enter the 1st string")
    #str2 = input(" enter the 2nd string")
    str1 = "public relations"
    str2 = "crap built on lies"

    print(AnagramChecker(str1, str2))






