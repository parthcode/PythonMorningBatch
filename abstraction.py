"""
This is a concept by which you cannot create any object for a class

1.Client server atch
2.Polymorphism
3.request , json and xml(Flask framework)
"""

from abc import ABC, abstractmethod


class Python(ABC):

    @abstractmethod
    def display_python(self):
        print("This is python")


obj = Python()
obj.display_python()
