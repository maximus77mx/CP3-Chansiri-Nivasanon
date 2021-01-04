'''
ตัวแปรที่อยู่ใน f ทำงานแค่ใน Section นั้น
'''
correctNumber = 88
useGuess = 0
while useGuess != correctNumber:
    useGuess = int(input("Pls guess a number: "))
    if useGuess > correctNumber:
        print("Too Large")
    elif useGuess < correctNumber:
        print("Too Small")
    elif useGuess == correctNumber:
        print("Collect")
