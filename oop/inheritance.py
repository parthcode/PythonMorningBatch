"""

1.new user = > 1.user_name 2. new password
2.Store it into a file (user_details.txt)

1.login :
User name
password
if the above data is there in user_details.txt ==>access GRANTED
if not ==> ACCESS DENIED
"""


class Base:
    def __init__(self, user_name):
        self.name = user_name

    def base_display(self):
        print("Name is :", self.name)


class Child(Base):
    def child_display(self):
        print("This is a child class function")


name = input("Enter the name")
obj = Child(name)
obj.base_display()
