"""
1. Expected input format of array: ([1,2,3,4],7)
where array[0] = [1,2,3,4] <-- the array to find the pair in
array[1] = [4] <-- result

2. The variable called self.validation_set is being used to accommodate the edge case such as below:
[[1,3,2,2],4]
"""
class Array_sum_pair_2():
    def __init__(self, array):
        self.array = array
        self.lst = self.array[0]
        self.result = self.array[1]
        self.seen = set()
        self.target_pairs = set()
        self.validation_set = set()

    def __len__(self):
        return len(self.array)

    def display(self):
        return print(self.target_pairs)

    def ArraySumPairFinder(self):
        #edge case test
        if self.__len__() < 2:
            print(" Not enough elements to evaluate")
            return False

        #Driving logic
        for element in self.lst:
            pair_element = self.result - element #store the result - (element in list)
            if pair_element not in self.lst: #check if the  exists in the list
                self.seen.add(element) #adding to the seen set
            elif pair_element in self.lst and element not in self.seen:
                self.target_pairs.add(element)
        return self.target_pairs


if __name__ == "__main__":
    a = [[1,3,2,2], 4]
    #a = [[1,2,3,4], 7]
    #a = [[0], 14]
    d = Array_sum_pair_2(a)


