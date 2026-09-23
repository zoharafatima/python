# text=input("Enter text: ")
# count=0
# for i in text:
#     if i.lower() in 'aieou':
#         count+=1

# print("Number of vowels:", count)
'''q1'''
# list=[10,20,30,40,50]
# print("Original list:", list)
# list.append(60)
# print("After append:", list)
# list.insert(1,15)
# print("After insert:", list)
# list.sort()
# print("After sorting:", list)
# list.remove(40)
# print("After removing 40:", list)
'''q2'''
# text = input("Enter a sentence: ")
# words = text.split()
# frequency = {}
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
# print("Word frequency:")
# print(frequency)
'''*args and **kwargs'''
# def my_function(*numbers):
#     total=0
#     for num in numbers:
#         total=total+num
#     return total
# print(my_function(1,2,2,3,4,5))
'''*kwargs'''
# def my_function(**kid):
#     print("His last name is " + kid["lname"])
# my_function(fname="Ali", lname="Asgar")
'''next'''
# def my_function(username,**details):
#     print(f"Username: {username}")
#     for key, value in details.items():
#         print(f"{key}: {value}")
# print(my_function("Emily",age=25,city="New York",country="USA"))
'''unpacking'''
# def my_function(a,b,c):
#     return a+b+c
# numbers=[1,2,3]
# result=my_function(*numbers)
# print(result)

def user(fname,lname):
   print(f"Hello, {fname} {lname}!")
info={"fname":"Ali","lname":"Asgar"}
user(**info)