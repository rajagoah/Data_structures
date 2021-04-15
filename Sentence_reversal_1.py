class Sentence_reversal_1():
    def __init__(self, strng):
        self.strng = strng
        self.str = None
        self.counter = 0
        self.dic = dict()

    def __space_trimmer__(self):
        return self.strng.strip()

    def reverser(self):
        self.strng = self.__space_trimmer__()

        arr_temp = self.strng.split()
        for k in arr_temp:
            self.counter += 1
            if k not in self.dic:
                self.dic[self.counter] = k
        print(self.dic)

        arr_temp.clear()

        for i in self.dic:
            arr_temp.append(self.dic[self.counter])
            self.counter -= 1

        self.str = ' '.join(arr_temp)
        return self.str

if __name__ == "__main__":
    #a = 'Aakarsh Rajagopalan'
    #a = ' aakarsh rajagopalan '
    a = 'This is a good practice       '
    d = Sentence_reversal_1(a).reverser()
    print(d)