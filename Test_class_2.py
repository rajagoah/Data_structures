class test_class_2():

    def public(self):
        print(" this method will be prompted when using the dot operator")

    def _private(self):
        print(" this method will not be prompted when using the dot operator")

if __name__ == "__main__":
    ts = test_class_2()

    ts.public()

    ts._private()