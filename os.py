import os

# Specify the directory path
path = "."

# Get and print the contents of the directory
contents = os.listdir(path)

print("Directory contents:")
for item in contents:
    print(item)