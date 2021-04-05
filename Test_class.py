class test_class():
    def __init__(self, color, height):
        self.color = color
        self.height = height

    def print_color(self):
        return print('The color is: ', self.color)

    def print_height(self):
        return print('The height is: ', self.height)

if __name__ == "__main__":
    inst = test_class('green',3)

    inst.print_height()
    inst.print_color()

