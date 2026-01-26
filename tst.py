from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    pass

class B(A):
    @abstractmethod
    def hi():
        pass

class C(B):
    pass

obj = B()
print(type(B)) 
