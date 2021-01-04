'''
userInput = int(input("inputForm: "))
text = ""
for i in range(userInput):
    text = text + "*"
print(text)
'''
userInput = int(input("inputForm: "))
for i in range(userInput):
    print("*"*(i+1))

