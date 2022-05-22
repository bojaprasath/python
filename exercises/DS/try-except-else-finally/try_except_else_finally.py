try:
    a = 1
    print(a)
except:
    print('There is no a from except')
else:
    print('There is no a from else')
finally:
    print('There is no a from finally')

try:
    del a
    print(a)
except:
    print('There is no a from except')
else:
    print('There is no a from else')
finally:
    print('There is no a from finally')