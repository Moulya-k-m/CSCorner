class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print("Average= ",sum/ len(self.marks))

s1=student("Rohan",[97,96,98])
print(s1.name,s1.marks)
s1.avg()

s2=student("Mohan",[99,96,97])
print(s2.name,s2.marks)
s2.avg()
        