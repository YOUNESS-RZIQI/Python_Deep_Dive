class a():
    pass


class b(a):
    pass


class c(b):
    pass


class d(c):
    pass


print(d.mro())