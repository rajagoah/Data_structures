a = [[1,3,2,2],4]

lst = a[0]
result = a[1]

element = lst[0]
counter = 0

for k in range(len(lst)):
    print("k is: ", k)
    if k != (len(lst)-1):
        s = lst[k] + lst[k+1]
        if s == result:
            print(f"{lst[k]} + {lst[k+1]}".format(lst[k], lst[k+1]))
            counter += 1
        else:
            continue
    print(" the number of pairs is: ", counter)