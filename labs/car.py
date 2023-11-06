class SimpleCar:
    def __init__(self):
        self.miles = 0
        self.dist = 0
        
    def reverse(self):
        self.miles = self.miles - self.dist
        
    def get_odometer(self):
        return self.miles
    
    def honk_horn(self):
        print('beep beep')
        
    def report(self):
        print(f'Car has driven: {self.miles - self.dist} miles')
        
if __name__ == "__main__":
    # TODO: Create SimpleCar object
    # TODO: Drive input number of miles forward
    # TODO: Drive input number of miles in reverse
    # TODO: Honk the horn
    # TODO: Report car status
    
    car = SimpleCar()
    car.miles = int(input())
    car.dist = int(input())
    
    car.honk_horn()
    car.report()