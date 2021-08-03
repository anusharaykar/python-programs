class person:
    def hello(self,name=None,age=None):
        self.name=name
        self.age=age
        if(self.name!=None and self.age!=None):
            print("Hello %s and Age is %s"%(self.name,self.age))
        elif self.name!=None and self.age==None:
            print("Hello %s"%self.name)
        else:
            print("Hello")
p1=person()
p1.hello()
p1.hello('RVCE')
p1.hello('RVCE',25)
