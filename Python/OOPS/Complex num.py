class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def num(self):
        print(self.real,"i + ", self.imag,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return complex(newReal,newImag)

num1=complex(1,3)
num1.num()

num2=complex(4,6)
num2.num()

num3 = num1 +num2
num3.num()
