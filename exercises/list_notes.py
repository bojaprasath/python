a = [1,2,3,4,5,6]
b = a[0:2]
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))
b[0] = 0
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))
print(a)
print(b)

a = [1,2,3,4,5,6]
b = a
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))
b[0] = 0
print(id(a))
print(id(b))
print(id(a[0]))
print(id(b[0]))
print(a)
print(b)
import sys
print('Size in bytes : {}'.format(sys.getsizeof(a)))

