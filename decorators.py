# 2 types of decorators:
# - function decoratars (common)
# - class decoratars

from ast import arg
import functools
from inspect import signature
from unittest import result

def greeting(f):
    def welcome():
        print("welcome")
        f()
    return welcome

# @greeting
# def hello():
#     print("hello")

def hi():
    print("hi")

# this means same as:
new_hi = greeting(hi)
hi = new_hi

# hello()
hi()




# another example
def start_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@start_end_decorator
def print_name():
    print("Gagan")
    
# print_name = start_end_decorator(print_name)   # when @decorator_name is not written

print_name()



# with arguments
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(add5(10))




# another example with arguments, decorator with an argument
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"hello{name}")
    
greet("Alex")
    



# nested decorator

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
        signature = ",".join(args_repr + kwargs_repr)
        print(f"calling{func.__name__}({signature})") 
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

say_hello("Gagan")





# classs decorator
class CountCalls():
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)
        
@CountCalls
def say_hello():
    print("Hello")
    
say_hello()