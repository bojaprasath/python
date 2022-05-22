class A(object):
    def __init__(self):
        self.a = 'a'
    def who_am_ii(self):
        self.a = 'I am set in A'
        print("I am a A")
        print(self.b)  ## this is available to parent class

class C(object):
    def __init__(self):
        self.c = 'c'
    def who_am_ii(self):
        self.c = 'I am set in C'
        print("I am a C")
        print(self.b)  ## this is available to parent class

class B(A,C):
    def __init__(self):
        self.b = 'b'
        A.__init__(self)  # calling constrcutor of parent .. Explicity needed . Otherwise value will not be availabe in child
        C.__init__(self)
        super().__init__()
    def who_am_i(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print('callping parent')
        self.who_am_ii()
        print('calling A')
        A.who_am_ii(self)
        print('Calling C')
        C.who_am_ii(self)
        print("I am a B")
        print(self.a)
        print(self.b)
        print(self.c)

b = B()
# print(b.a)
# print(b.b)
# print(b.c)
b.who_am_i()
# b.who_am_ii()
# print(B.__mro__) # if class does not have A(object), __mro__ is failing ..
# print(B.__)

a = A()
print(a.a)
b = a
print(b.a)
print(id(a))
print(id(b))
b.a = 6
print(a.a)
print(b.a)

a = {'ip': '1'}
b = a
print(id(a))
print(id(b))
a = {'ip': '2'}
print(a)
print(b)

a = 1
b = a
print(id(a))
print(id(b))
b = 2
print(a)
print(b)
# def mod(a):
#     a = ['2']
#     print(a)
a = ['1']
b = a
print(id(a))
print(id(b))
# mod(a)
print(a)
print(b)
a = ['3']
print(a)
print(b)
print(id(a))
print(id(b))


input = [0,1,1,1,1,0,0]
index0 = input.index(0)
index1 = input.index(1)
for i in input:
    if i == 0:
        if index0 == input.index(i):
            continue
        else:
            input[index0+1] = i
            index0 = index0 +1
    if i == 1:
        if index1 == input.index(i):
            continue
        else:
            input[index1+1] = i
            index1 = index1 +1
print(input)