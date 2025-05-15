def add(*args):
    a = 0
    for n in args:
        a = a +n
    print(a)
add(3,5,6)

def calculate(n,**kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)


calculate(2, add= 3, multiply=5)


class Car:

    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan",model="GTR")
