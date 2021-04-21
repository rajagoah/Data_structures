class contiguous_sum():
    def __init__(self, arr):
        self.arr = arr
        self.current_sum = self.max_sum = self.arr[0]

    def contiguous_sum_arr_finder(self):
        #edge case 1
        if len(self.arr) == 0:
            return 0

        #edge case 2
        if len(self.arr) == 1:
            return self.arr[0]

        #driver logic
        for num in self.arr[1:]:
            self.current_sum = max(self.current_sum + num, self.max_sum)
            self.max_sum = max(self.current_sum, self.max_sum)

        return self.max_sum

if __name__ == "__main__":
    #a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #a = [1,2,-3]
    a = [1, 2, -1, 3, 4, 10, 10, -10, -1]
    d = contiguous_sum(a).contiguous_sum_arr_finder()
    print(d)
