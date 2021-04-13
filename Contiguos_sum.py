a = [-2,1,-3,4,-1,2,1,-5,4]
#a = [1,2,3,4,5]

sum_now= 0
arr = [None]

for k in range(len(a)):
    if k != (len(a) - 1):
        sum_now = a[k] + sum_now
        if None in arr or sum_now > arr[0]:
            arr[0] = sum_now
    k += 1
print(arr)