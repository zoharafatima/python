text=input("Enter text: ")
count=0
for i in text:
    if i.lower() in 'aieou':
        count+=1

print("Number of vowels:", count)
        