def add(*args):   #Takes any number of arguments that are passed --- Unlimited positional arguments
    print(args[1])      #Can get any value by indexing
    for i in args:          #All the arguments are in a form of tuple
        i+=i
    print(i)
add(10,20,30,40,50)


def cal(**kwargs):          #Takes any number of keyword arguments
    print(kwargs)       #All the arguments are in form of dictionary
    for key,value in kwargs.items():
        print(key)
        print(value)
cal(add = 5, mul = 10)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Rolls Royce", model = "Ghost")
print(my_car.model)