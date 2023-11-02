def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    
    
    cost = miles_per_gallon / miles_driven
    price = dollars_per_gallon / cost
    
    print(f'{price:.2f}')
    return price
    
if __name__ == '__main__':
    # Type your code here.
    miles_per_gallon = float(input())
    gas_cost = float(input())
    
    driving_cost(miles_per_gallon, gas_cost, 10)
    driving_cost(miles_per_gallon, gas_cost, 50)
    driving_cost(miles_per_gallon, gas_cost, 400)