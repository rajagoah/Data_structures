a = [[1,3,2,2], 4]

lst = a[0]
result = a[1]
seen = set()
target_pairs = set()

for element in lst:
    pair_element = result - element
    if pair_element not in lst:
        seen.add(element)
    elif pair_element in lst:
        target_pairs.add((element, pair_element))

print(target_pairs)




