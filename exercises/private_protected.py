### Protected variables can be printed and modified using self._var
### Private variables can be accessed using obj._<class>__<variable>
### After this , private variables can be printed

class School:
    #school = 'st xaviers'
    def __init__(self,location):
        self.location = location
        self._school = 'st xaviers'

class Student(School):

    def __init__(self,name,location):
        self.name = name
        self.place = location
        School.__init__(self,location)

s1 = Student('name','hosur')
print(s1._school)


class employee:
    def __init__(self, name, sal):
        self.__name=name  # private attribute
        self.__salary=sal # private attribute
        self.__location = 'hosur'


e1 = employee("Bill",10000)
e1.__salary = 20000
print(e1.__salary)
# e1.__location = 'bgl'
print(e1._employee__location)

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

@Computer
def setOfferPrice(price):
    self.__offer = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
print(c.__maxprice)
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()