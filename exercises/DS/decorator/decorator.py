# def decorated(func):
#     print('decorated')
#     return func
#
# def decorated1(func):
#     print('decorated1')
#     return func
#
# @decorated
# @decorated1
# def func():
#     print("Base function call")
#
# func()

def decorated(func):
    def inner():
        print('decorated')
        output = func()
        return  output

    return inner

def decorated1(func):
    def inner1():
        print('decorated again')
        output = func()
        return output
    return inner1

@decorated
@decorated1
def func():
    return "Base function call"

print(func())

def hello_decorator(func):


    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        print(args)
        returned_value = func(*args, **kwargs)
        print("after Execution")
        # returning the value to the original frame
        return returned_value


    return inner1

def hello_decorator1(func):


    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        print(args)
        returned_value = func(*args, **kwargs)
        print("after Execution")
        # returning the value to the original frame
        return returned_value


    return inner1

# adding decorator to the function
@hello_decorator
@hello_decorator1
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b


a, b = 1, 2

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))