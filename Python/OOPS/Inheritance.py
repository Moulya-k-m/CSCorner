class employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal

    def ShowDetails(self):
        print("Role = ",self.role)
        print("Dept = ",self.dept)
        print("Salary = ",self.sal)

class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super(). __init__("Asst.Manager","IT","100000")

eng1=engineer("Mohan",31)
eng1.ShowDetails()