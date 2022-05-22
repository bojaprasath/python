class A(object):
    def who_am_i(self):
        print("I am a A")

class B(A):
    def who_am_i(self):
        print("I am a B")

class C(A):
    def who_am_i(self):
        print("I am a C")

class D(B,C):
    def who_am_i(self):
        print("I am a D")

d1 = D()
d1.who_am_i()
d2 = d1
# del d1
d2.who_am_i()
print(D.__mro__)