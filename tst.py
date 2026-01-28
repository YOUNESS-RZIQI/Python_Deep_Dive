# import builtins  

# print(hasattr(builtins, "print"))

class b():
    hello = "hellow"

def hi():
    print("hi")

a = type("A", (b,), {"hi": hi})


print(a.__name__)