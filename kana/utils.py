# # https://stackoverflow.com/questions/128573/using-property-on-classmethods, Retrieved October, 2023.
# from functools import cached_property

from const import IterSymbol

# This is temporarily somewhere for testing code structure ideas

class A:

    def __init__(self, c: list):
        self.c = c

    def add(self, other):
        new_c = self.c + [other]
        return self.__class__(c=new_c)


class B(A):
    pass


a = A([1, 2])
b = a.add(3)
print(b.c)

a2 = B([1, 2])
b2 = a2.add(4)
print(b2.c)
print(type(b2))