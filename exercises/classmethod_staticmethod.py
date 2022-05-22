class Student:
    average = 70
    def __init__(self,name,location):
        self.name = name
        self.location = location

    @classmethod
    def change_school(cls,average):
        cls.average = average

    @staticmethod
    def isFirstClass(average):
        if average > Student.average:
            return True
        return False

s1 = Student('asad','asdsad')
s2 = Student('xyz','asdsad')

class Student(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

scott = Student('Scott',  'Robinson')



class Student(object):

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

scott = Student.from_string('Scott Robinson')

