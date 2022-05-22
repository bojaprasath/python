class A(object):
		def function1(self):
				print('function of class A')
class B(A):
		def function1(self):
				print('function of class B')
				super(B, self).function1()
class C(B):
    def function1(self):
        print('function of class C')
        super(C, self).function1()
j = C()
j.function1()
'''
function of class C
function of class B
function of class A
'''

class Square:
    def __init__(self,side):
        self.side = side
        print(self.side)

    def area(self):
        return self.side * self.side

class Cube(Square):
    def __init__(self,side):
        self.side = side
        Square.__init__(self,side)
        # super().__init__(7) #Equivalent to above code
    def area(self):
        return super().area() * 6

    def volume(self):
        return super().area() * self.side

c = Cube(6)
print(c.volume())
# import pdb;pdb.set_trace()
# print(dir(c))


# first parent class
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    # second parent class


class Employee(object):
    def __init__(self, salary, post):
        self.salary = salary
        self.post = post

    # inheritance from both the parent classes


class Leader(Person, Employee):
    def __init__(self, name, idnumber, salary, post, points):
        self.points = points
        Person.__init__(self, name, idnumber)
        Employee.__init__(self, salary, post)
        print('salary : {}' .format(self.salary))


ins = Leader('Rahul', 882016, 75000,'Assistant Manager', 560)
