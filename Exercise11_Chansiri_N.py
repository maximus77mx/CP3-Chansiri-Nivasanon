userInput = int(input(": "))
for i in range(userInput):
    print(" " *(userInput - i -1) + ("*" * (2 * i +1)))
