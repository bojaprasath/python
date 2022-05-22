def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i * i
        i += 1  # Next execution resumes
        # from this point


# Driver code to test above generator
# function
for num in nextSquare():
    if num > 100:
        break
    print(num)

def nextsquare(x):
    for i in range(x):
        yield i * i

gen = nextsquare(3)
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))


def cube(y):
    return y * y * y;


g = lambda x: x * x * x
print(g(5))

print(cube(5))


def addition(n):
    return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
print(map(cube,numbers))


lambda addition: addition + addition
result = map(addition, numbers)
print(list(result))

# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)





