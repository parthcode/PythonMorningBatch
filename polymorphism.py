class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        # print("Name is :", self.name)
        return self.name


def caller(*obj):
    x = [i.display() for i in obj]
    print(x)
    # for i in obj:
    #     i.display()


obj = Student('alex')
obj1 = Student('Lexi')
caller(obj, obj1)
