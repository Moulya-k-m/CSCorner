class circle:
    def __init__(self,radi):
        self.radi=radi

    def area(self):
        return 3.14*self.radi**2

    def peri(self):
        return 2*3.14*self.radi

c1=circle(10)
print(c1.area())
print(c1.peri())

    