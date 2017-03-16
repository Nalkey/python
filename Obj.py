class Person(object):
    """
    返回Person对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name


class Student(Person):
    """
    返回Student对象，name, branch, year
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
    返回Teature对象，name，数组->字符串
    """

    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


person1 = Person('L')
student1 = Student('eigh', 'EPG', 2010)
teacher1 = Teacher('ton', ['E', 'P', 'G'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
