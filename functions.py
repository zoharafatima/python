# class prime:
#     def ISprime(self,n):
#         is_prime=True
#         for i in range(2,n):
#             if n%i==0:
#                 is_prime=False
#         return is_prime

# N=int(input("Enter N:"))

# obj=prime()
# result=obj.ISprime(N)
# print(result)
# ______________________________________________
# def GRADE_calculations(marks):
#     if marks>=90:
#         return "A"
#     elif marks>=80:
#         return "B"
#     elif marks>=70:
#         return "C"
#     elif marks>=60:
#         return "D"
#     else:
#         return "F"
# marks=int(input("Enter marks:"))
# result=GRADE_calculations(marks)
# print(result)
# ______________________________________________
'''q'''
# numbers = [10, 20, 30, 40]
# print("Original list:", numbers)
# numbers.append(50)
# print("After append:", numbers)
# numbers.insert(1, 15)
# print("After insert:", numbers)
# numbers.remove(30)
# print("After remove:", numbers)
# numbers.sort()
# print("After sorting:", numbers)
#_______________________________________________
'''q2'''
# import numbers
# numbers = (10, 20, 30, 20, 40) 
# print("Tuple:", numbers)
# print("Length:", len(numbers))
# print("First element:", numbers[0])
# print("Last element:", numbers[-1])
# print("Count of 20:", numbers.count(20))
# print("Position of 30:", numbers.index(30)) 

'''q3'''
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)