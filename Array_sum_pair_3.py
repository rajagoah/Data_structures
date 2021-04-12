"""
Input array format = [[1,2,3,4],7]

"""
class Array_sum_pair():

    def __init__(self, array):
        self.lst = array[0]
        self.seen = set()
        self.output = set()
        self.result = array[1]

    def pair_finder(self):
        for element in self.lst:
            target_pair = self.result - element
            if target_pair not in self.seen: #if the value of target_pair is not in the seen set, then add it
                self.seen.add(element)
            else: #if it is in the seen set, then insert a tuple containing max and min of the element in the iteration and the value of target pair
                self.output.add((max(element, target_pair), min(element, target_pair)))
        return self.output

if __name__ == "__main__":
    #a = [[1,3,2,2],4]
    #a = [[1,2,3,4],7]
    a = [[7,0],7]
    d = Array_sum_pair(a).pair_finder()
    print(d)
