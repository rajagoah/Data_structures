class unique_characters_in_string():

    def __init__(self, input):
        self.input = input
        self.seen = set()
        self.output = set()

    def __len__(self):
        return len(self.input)

    def unique_or_not(self):

        leng = self.__len__()

        #edge case 1
        if leng == 0:
            return 0

        #edge case 2
        if leng == 1:
            return self.input

        #driver logic
        for i in self.input:
            if i not in self.seen:
                self.seen.add(i)
            else:
                self.output.add(i)

        if len(self.output) > 0:
            return 0
        else:
            return 'Unique strings'

if __name__ == "__main__":
    a = 'abac'
    d = unique_characters_in_string(a).unique_or_not()
    print(d)


