#https://www.journaldev.com/14893/python-property-decorator
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks'

    # This will get the DB output from propery gotmarks and parse in property.setter and set the results to object
    @gotmarks.setter
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks

#Instead of calling got marks explicity , it calls automatically for object value change
st = Student('st1','25')
print(dir(st))
print('name : {} marks: {} gotmarks : {} '.format(st.name,st.marks,st.gotmarks))
st.name = 'st2'
print(dir(st))
print('name : {} marks: {} gotmarks : {} '.format(st.name,st.marks,st.gotmarks))


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.gotmarks = self.name + ' obtained ' + self.marks + ' marks'

    @property
    def gotmarks(self):
        #In this place we can call DB to get the data and set the results to the object
        self.result = self.name + ' obtained ' + self.marks + ' marks'



#Instead of calling got marks explicity , it calls automatically for object value change
st = Student('st1','25')
print(dir(st))
st.gotmarks
print('name : {} marks: {} gotmarks : {} '.format(st.name,st.marks,st.result))
st.name = 'st2'
# st.gotmarks is not called explicitly and called as it is property
print('name : {} marks: {} gotmarks : {} '.format(st.name,st.marks,st.result))

#when property is used , any change in object will trigger the property.


####### property function ########
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)
t = Celsius()
print(t.temperature)
t.temperature = 5
t.to_fahrenheit()
