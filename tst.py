


class A(type):
    def __repr__(cls):
        return "<class 'A'>"
    pass

class B(metaclass=A):
    pass

print(type(A)) 
