from abc import ABC, abstractmethod


class a(ABC):

    def say_hi():
        print("Hi")
    say_hi = abstractmethod(say_hi)


class b(a):
    say_hi = "hi"


print(b().say_hi)