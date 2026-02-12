class a():
    def __init__(self, id):
        self.id = id


o1 = a(1)
o2 = a(2)
o3 = a(3)
ls = [o1, o2, o3]

new = sorted(ls, key=lambda a: a.id)


for a in new:
    print(a.id)