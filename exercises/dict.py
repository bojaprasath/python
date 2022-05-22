a = {}
a[1] = {}
a[1]['name'] = 'a'
a[2] = {}
a[2]['name'] = 'b'
print(a)
print(a.keys())
for key in a.keys():
    print(key)
print('ITEMS')
print(a.items())
keys = ['a','e','i','o','u']
print(dict.fromkeys(keys))
print(a.get(1))
print(a.has_key(1))
b = a.iteritems()
print(next(b))
print(next(b))
print(a.setdefault('3'))
print(a.values())
print('pop')
print(a.pop(1))
print(a)
print('pop item')
print(a.popitem())
print(a)

# a = (1,2,3,4)
# print(type(a))