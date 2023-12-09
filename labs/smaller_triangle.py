class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print(f"Base: {self.base:.2f}")
        print(f"Height: {self.height:.2f}")
        print(f"Area: {self.get_area():.2f}")


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    # TODO: Read and set base and height for triangle1 (use set_base() and set_height())
    t1input_1 = float(input("Enter the base for triangle 1: "))
    t1input_2 = float(input("Enter the height for triange 1: "))

    triangle1.set_base(t1input_1)
    triangle1.set_height(t1input_2)

    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())
    t2input_1 = float(input("Enter the base for triangle 2: "))
    t2input_2 = float(input("Enter the height for triangle 2: "))

    triangle2.set_base(t2input_1)
    triangle2.set_height(t2input_2)

    print("Triangle with smaller area:")

    if triangle1.get_area() > triangle2.get_area():
        print(f"Base: {t2input_1:.2f}")
        print(f"Height: {t2input_2:.2f}")
        print(f"Area: {triangle2.get_area():.2f}")
    else:
        print(f"Base: {t1input_1:.2f}")
        print(f"Height: {t1input_2:.2f}")
        print(f"Area: {triangle1.get_area():.2f}")

    # TODO: Determine smaller triangle (use get_area())
    #       and output smaller triangle's info (use print_info())
