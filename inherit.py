class student:
    def __init__(self,usn=None,name=None,age=None):
        self.usn=usn;
        self.name=name
        self.age=age
    def getdata(self):
        self.usn=input("enter usn");
        self.name=input("enter name:");
        self.age=int(input("enter age:"))
    def display(self):
        print("usn=",self.usn)
        print("name=",self.name)
        print("age=",self.age)
class pgstudent(student):
    def __init__(self,sem=None,fees=None,stipend=None):
       # super().__init__(usn,name,age)
        self.sem=sem;
        self.fees=fees
        self.stipend=stipend
    
    def pggetdata(self):
        self.sem=input("enter semester");
        self.fees=int(input("enter fees:"));
        self.stipend=int(input("enter stipend:"))
    def pgdisplay(self):
        print("sem is:",self.sem)
        print("fees:",self.fees)
        print("stipend is:",self.stipend)
class ugstudent(student):
    def __init__(self,sem=None,fees=None,stipend=None):
        #super().__init__(usn,name,age)
        self.sem=sem;
        self.fees=fees
        self.stipend=stipend
    
    def uggetdata(self):
        self.sem=input("enter semester");
        self.fees=int(input("enter fees:"));
        self.stipend=int(input("enter stipend:"))
    def ugdisplay(self):
        print("sem is:",self.sem)
        print("fees:",self.fees)
        print("stipend is:",self.stipend)
obj1=pgstudent()
obj2=ugstudent()
print("enter details of pgstudent");

obj1.getdata()
obj1.pggetdata()
obj1.display()
obj1.pgdisplay()
print("enter details of ugstudent");

obj2.getdata()
obj2.uggetdata()
obj2.display()
obj2.ugdisplay()
