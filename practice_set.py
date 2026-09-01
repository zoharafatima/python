#this is the first question
# name=input("Enter your name: ")
# print("Good morning" +" "+ name)
#---------------------------------------------------
#question 2
# from datetime import datetime
# name=input("Enter your name: ")
# date=datetime.now()
# print(f'''Dear {name},
#       You are selected!
#       Date: {date}
#       ''')
#---------------------------------------------------
#question 3
# text=input("Enter your text: ")
# count=0
# if "  " in text:
#     print("double space found")
# else:
#     print("double space not found")

#---------------------------------------------------
#question 4
text=input("Enter your text: ")
text=text.replace("  "," ") #strings are immutable
print(text)
