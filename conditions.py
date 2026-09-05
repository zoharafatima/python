# day=int(input("Enter number:"))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
# _________________________________________________
# sub1=int(input("Enter marks of math: "))
# sub2=int(input("Enter marks of physics: "))
# sub3=int(input("Enter marks of chemistry: "))
# math=sub1*100/100
# phy=sub2*100/100
# chem=sub3*100/100
# total=(math+phy+chem)/3
# if(total>=40 and math>=33 and phy>=33 and chem>=33):
#     print("You have passed the exam.")
# else:
#     print("You have failed the exam.")

# _____________________________________________________
# p1="Make a lot of money"
# p2="Buy now, pay later"
# p3="subscribe this"
# p4="Click this link"
# comments=input("Enter your comment: ")
# if(p1 in comments or p2 in comments or p3 in comments or p4 in comments):
#     print("This is a spam comment.")
# else:
#     print("This is not a spam comment.")
# ________________________________________________________
'''length checker'''
name=input("Enter user name:")
if(len(name)<10):
    print("Your username has less than 10 characters.")
else:
    print("User name valid.")