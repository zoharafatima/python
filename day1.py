a=int(input("enter a number"))
b=int(input("enter a number"))
print("\nchoose the operation you want to perform")
print("\n1.addition\n2.subtraction\n3.division\n4.multiplication\n5.modulus")
choice=int(input("enter your choice"))
if(choice==1):
    print(f"addition of {a} & {b} is {a+b}")
if(choice==2):
    print(f"subtraction of {a} & {b} is {a-b}")
if(choice==3):
    print(f"division of {a} & {b} is {a/b}")
if(choice==4):
    print(f"multiplication of {a} & {b} is {a*b}")
if(choice==5):
    print(f"modulus of {a} & {b} is {a%b}")
