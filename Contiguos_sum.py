class Contiguous_sum():

    def __init__(self, array):
        self.a = array
        self.ending_slice = 0 #in order to extract the subset that results in highest contiguous sum
        self.result_array = []  # to store the subset resulting in the highest contiguous sum
        self.sum_now = 0 #to store the contiguous sum
        self.arr = [None] #to store the values in the contiguous sum

    def contiguous_sum_array_finder(self):
        for k in range(len(self.a)):
            self.sum_now = 0
            for l in self.a[k:]:
                self.sum_now = l + self.sum_now
                if (None in self.arr) or (self.sum_now > self.arr[0]):
                    self.ending_slice = self.a[k:].index(l)
                    self.result_array = self.a[k:]
                    self.result_array = self.result_array[:self.ending_slice + 1]
                    self.arr[0] = self.sum_now
        return self.arr[0], self.result_array

if __name__ == "__main__":
    a = [-2,1,-3,4,-1,2,1,-5,4]
    d = Contiguous_sum(a).contiguous_sum_array_finder()
    print(d)
