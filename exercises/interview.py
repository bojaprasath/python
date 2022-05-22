class student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_name(obj):
        return obj.name


st1 = student('asdasd', 'asdsada')
print(st1.get_name())

def fibino(n):
    if n==0:
	    return 0
    elif n == 1:
	    return 1
    return fibino(n-1)+fibino(n-2)

print(fibino(3))


def square(num):
	return num**2

l=list(range(5))
lis=list(map(square,l))
print(lis)

def even(num):
	return num%2 == 0
lis=list(map(even,l))
val = list(filter(even,l))
print(lis)
print(val)