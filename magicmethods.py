class Oper:
    def __init__(self):
        self.alist=[]

    def get_elements(self):
        n=int(input("enter the size of the list"))
        for i in range(0,n):
            self.alist.append(int(input("enter the element")))
    def __add__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
              new_list.append(self.alist[i]+other.alist[i])
        return new_list
    def __sub__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
              new_list.append(self.alist[i]-other.alist[i])
        return new_list
    def __mul__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
              new_list.append(self.alist[i]*other.alist[i])
        return new_list
    def __div__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
              new_list.append(self.alist[i]/other.alist[i])
        return new_list
    def __floordiv__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
              new_list.append(self.alist[i]//other.alist[i])
        return new_list
    
              
              
