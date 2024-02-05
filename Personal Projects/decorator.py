def convert_upper(f):
    print("convert_upper")
    def wrap(*args, **kwargs):
        print("wrap")
        x = f(*args, **kwargs)
        return x.upper()
    return wrap

@convert_upper
def my_name(name):
    return name
name = input("What's your name? ")
print(my_name(name))
