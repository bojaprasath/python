#Class method
class employee:
    num_employees = 0
    raise_amount = 1.04
    def __init__(bd,first,last,pay):
        bd.first = first
        bd.last = last
        bd.pay = pay
        bd.email = first + '.' + last + '@gmail.com'
        employee.num_employees = employee.num_employees + 1
    def fullname(bd):
        return bd.first + ' ' + bd.last
    def apply_raise(bd):
        bd.pay = int(bd.pay * employee.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, amount = emp_str.split('-')
        return cls(first,last,int(amount))





emp1 = employee('first1', 'last1', 50000)
emp1 = employee('first2', 'last2', 60000)
print(employee.raise_amount)
print(emp1.raise_amount)
print(emp1.raise_amount)
'''
1.04
1.04
1.04
'''

employee.set_raise_amount(1.05)
print(employee.raise_amount)
print(emp1.raise_amount)
print(emp1.raise_amount)
'''
1.05
1.05
1.05
'''

emp_str_1 = 'str1-last1-50000'
first,last,amount = emp_str_1.split('-')
str_emp1 = employee(first,last,int(amount)) #Every time we need to split and call for each object
emp_str_2 = 'str2-last2-60000'
str_emp2 = employee.from_string(emp_str_2)
print(dir(str_emp2))



class A:
    college = 'NH'
    def __init__(self,name):
        self.name = name