import time





def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

def say_bye():
    print("bye")

def say_greeting():
    print("How are you?")

decorated_function = delay_decorator(say_greeting)

decorated_function()