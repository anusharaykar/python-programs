import os
from magicmethods import *
os.system('clear')
ov1=Oper()
ov2=Oper()
ov1.get_elements()
print(ov1.alist)
ov2.get_elements()
print(ov2.alist)
while True:
    print("1.overload +operator")
    print("2.overload -operator")
    print("3.overload *operator")
   
    print("4.overload //operator")
    ch=int(input("enter your choice"))
    if ch ==1:
        print("overloading + operator")
        print(ov1+ov2)
    elif ch==2:
        print("overloading - operator")
        print(ov1-ov2)
    elif ch==3:
        print("overloading *operator")
        print(ov1*ov2)
   
    elif ch==4:
        print("overloading // operator")
        print(ov1//ov2)
    else:
        print("invalid choice")
