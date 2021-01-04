inputround = int(input("Pls, Enter Number : "))
sum = 0
for x in range(inputround):
    inputNumber = int(input("x"+str(x+1)+":"))
    sum += inputNumber
print("Total =" , sum)