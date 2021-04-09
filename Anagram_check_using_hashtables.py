def AnagramChecker(str1, str2):

    str1.replace(' ','').lower() #replacing spaces with empty string
    str2.replace(' ','').lower() #replacing spaces with empty string

    #really good check to prevent the evaluation of below code
    if len(str1) != len(str2):
        return False
    
    d1 = {} #declaring 1st empty dictionaries
    d2 = {} #declaring 2nd empty dictionaries
    counter = 1 #declaring a counter variable to store the num of occurence of a letter

    for k in str1:
        #validating for d1
        if k not in d1.keys():
            d1[k] = counter
            counter =+1
        elif k in d1.keys():
            d1[k] = d1[k]+1

    for l in str2:
        # validating for d2
        if l not in d2.keys():
            d2[l] = counter
            counter =+1
        elif l in d2.keys():
            d2[l] = d2[l]+1

    return d1 == d2



if __name__ == "__main__":
    str1 = input(" enter the 1st string")
    str2 = input(" enter the 2nd string")

    print(AnagramChecker(str1, str2))






