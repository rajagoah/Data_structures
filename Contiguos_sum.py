a = [-2,1,-3,4,-1,2,1,-5,4]
#a = [4,-1,2]

index_position = 0
sum_now= 0
arr = [None]
result_array = [None]

for k in range(len(a)):
    sum_now = 0
    for l in a[k:]:
        sum_now = l + sum_now
        if (None in arr) or (sum_now > arr[0]):
            arr[0] = sum_now
print(arr[0])

