import itertools
data = [5, 2, 6, 4, 5, 9, 1]
result = itertools.accumulate(data)
for each in result:
    print(each)


shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations(shapes, 2)
for each in result:
    print(each)

shapes = ['circle', 'triangle', 'square',]
result = itertools.combinations_with_replacement(shapes, 3)
for each in result:
    print(each)

for i in itertools.count(10,3):
    print(i)
    if i > 20:
        break
print(list(range(10,20,2)))
out = itertools.count(10,3)