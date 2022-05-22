class employee:
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal

emp = employee('Emp1','20000')
print(emp.name)
print(emp.salary)


# defining a child class
class HR(employee):
    # def __init__(self):
    #     pass
    # member function task
    def task(self):
        print("We manage Employees")

hrEmp = HR("Captain", 10000)
print(hrEmp.salary)
print(hrEmp.name)
hrEmp.task()



######If child class does not have constructor , object creation of child uses constructor of parent


# defining a child class
class HR(employee):
    def __init__(self):
        pass
    # member function task
    def task(self):
        print("We manage Employees")


# hrEmp = HR()
# print(hrEmp.salary)
# print(hrEmp.name)
# hrEmp.task()

print('##PROTECTED #')
#PROTECTED
class employee:
    def __init__(self, name, sal):
        self._name=name
        self._salary=sal


# defining a child class
class HR(employee):
    # def __init__(self):
    #     pass
    # member function task
    def task(self):
        print("We manage Employees")

hrEmp = HR("Captain", 10000)
print(hrEmp._salary)
print(hrEmp._name)
hrEmp.task()
hrEmp._salary = 20000
print(hrEmp._salary)

print('#PRIVATE#')
##PRIVATE
class employee:
    def __init__(self, name, sal):
        self.__name=name
        self.__salary=sal


# defining a child class
class HR(employee):
    # def __init__(self):
    #     pass
    # member function task
    def task(self):
        print("We manage Employees")

emp = employee('namne','123213')
print(dir(emp))
print(emp._employee__name)
hr = HR("Captain", 10000)
print(hr._employee__name)