menuList = []
def showBill():
    sum = 0
    ending = "Thank you"
    print("Your Order".center(20,"*"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1], "THB")
        sum += int(menuList[number][1])
    print("Total Price(THB) : ",sum)
    print(ending.center(20,"*"))

while True:
    menuName = input("Pls,Enter Menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName,menuPrice])

showBill()

'''
def sumPrice():
    sum = 0
    for price in priceList:
        sum = sum + int(price)
    print("Total :", sum, "THB")
'''
