a = 'AAaaBBCcccccx01982'

counter = 1

dic = dict()
strng = list()

for k in range(len(a)):
    if a[k] not in dic:
        dic[a[k]] = counter
    else:
        dic[a[k]] = dic[a[k]] + 1

print(dic)
str
for k,v in dic.items():
    strng.append(k+ str(v))
print(''.join(strng))




