marks={
    "Rabia":90,
    "Ayesha":80,
    "Varun":70,
}
# print(marks["Rabia"])
# print(marks.items())
# print(marks["Varun"])
# print(marks.keys())
# print(marks.values())

# s={5,6,7,"Harry"}
# print(s,type(s))

# ______________________________________________________
'''practise set'''
# translation={
#     "Mubarak ho":"congratulations",
#     "Aayeh":"come",
#     "kya":"what",
#     "kab":"when",
#     "madad":"help",
# }
# word=input("Enter the word you want to translate: ")
# print(translation[word])
# ___________________________________________________
'''question 2'''
# n=int(input("Enter the no of elements: "))
# s=set()
# for i in range(8):
#     element=int(input("Enter the element: "))
#     s.add(element)
# print(s)
# _____________________________________________________
'''question 3'''
# s={18,'18'}
# print(s,type(s))
# ______________________________________________________
'''question 4'''
# q=set()
# q.add(18)
# q.add('18')
# q.add(18.00)
# print(q)
# _________________________________________________________
'''question 5'''
d={}
for i in range(4):
    name=input("Enter the name: ")
    lang=input("Enter the language: ")
    d[name]=lang
print(d)
