class Modal:
    def __init__(self, name):
        self.name = name
        self.color = ''

class Menu(Modal):
    def __init__(self, name, **kwargs):
        super().__init__(name)
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def set_color(self, color):
        self.color = color

x = ["john", "doe"]
py = []
for i in x:
    py.append(Menu(i, black="black"))
[py.set_color("blue") for py in py]
for i in py:
    print(i.black)

for i in py:
    for y in dir(i):
        print(i.__dict__)
        if not y.startswith("_"):
            print(getattr(i, y))


