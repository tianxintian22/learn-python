#coding=utf-8
class Person(object):
    address = 'Earth'
    count = 0
    def __init__(self, name, gender, birth, score):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__job = 'Student'
        self.__socre = score
        Person.count += 1

    def get_score(self):
        return self.__socre

    def get_grade(self):
        if self.__socre >= 90:
            return u'优秀'
        elif self.__socre >= 60:
            return u'及格'
        else:
            return u'不及格'

    @classmethod
    def how_many(cls):
        return cls.count


# p1 = Person()
# p1.name = 'Bart'

# p2 = Person()
# p2.name = 'Adam'

# p3 = Person()
# p3.name = 'Lisa'

# L1 = [p1, p2, p3]
# L2 = sorted(L1, lambda p1, p2:cmp(p1.name, p2.name))

# print L2[0].name
# print L2[1].name
# print L2[2].name

Person('xiaohong', 'Female', '1991-01-01', 90)
xiaoming = Person('xiaoming', 'Male', '1990-10-1', 85)
xiaoming.address = u'山东'
print xiaoming.name
# print xiaoming.__job
# print xiaoming.__socre
print xiaoming.address
print Person.address
print Person.count

print xiaoming.get_score()
print xiaoming.get_grade()
print xiaoming.get_grade


# 类方法
print  Person.how_many()
p4 = Person('xiaolan', 'Female', '1989-10-12', 60)
print Person.how_many()

print dir(xiaoming)