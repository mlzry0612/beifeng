class Student(object):
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def getMaxCourse(self):
        print(self.course.index(60))
        return max(self.course)


if __name__ == '__main__':
    s1 = Student("eric", 23, [30, 50, 60])
    print(s1.getMaxCourse())
