#coding=utf-8
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name,gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course
print isinstance(t, Person)

print type(t)
print dir(t)
print getattr(t, 'name')
setattr(t, 'name', 'Admin')
print t.name
print getattr(t, 'age', 10)