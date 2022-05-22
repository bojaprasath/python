
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

out = ordinary()


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)
divide(2,0)

#https://www.youtube.com/watch?v=pr1xfd6oTwY
import random
def power_of(arg):

    def decorator(fnc):
        # import pdb;
        # pdb.set_trace()
        def inner():
            print(exponent)
            return fnc() ** exponent
        return inner
    if callable(arg):
        exponent = 2
        # import pdb;
        # pdb.set_trace()
        return decorator(arg)

    else:
        exponent = arg
        # import pdb;
        # pdb.set_trace()
        return decorator

@power_of(3)
def random_odd_digit():
    out = random.choice([1,3,5,6])
    print(out)
    return out

print(random_odd_digit())

@power_of
def random_odd_digit():
    out = random.choice([1,3,5,6])
    print(out)
    return out

print(random_odd_digit())


#
# def decorator(argument):
#     def real_decorator(function):
#         def wrapper(*args):
#             for arg in args:
#                 assert type(arg)==int,f'{arg} is not an interger'
#             result = function(*args)
#             result = result*argument
#             return result
#         return wrapper
#     return real_decorator
#
