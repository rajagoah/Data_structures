class missing_element():

    def __init__(self, array):
        self.a = array[0]
        self.b = array[1]
        self.not_present = set()

    def missing_element_finder(self):
        for element in self.a:
            if element in self.b:
                continue
            else:
                self.not_present.add(element)
        return self.not_present

if __name__ == "__main__":
    arr = [[1,2,3,4,5,6,7],[7,6,4,3,1]]
    d =  missing_element(arr).missing_element_finder()
    print(d)

