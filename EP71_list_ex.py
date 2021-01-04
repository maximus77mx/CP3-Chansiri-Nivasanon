menuList = []
priceList = []
def showBill():
    print("---Your Order---")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
def sumPrice():
    sum = 0
    for price in priceList:
        sum = sum + int(price)
    print("Total :", sum, "THB")

while True:
    menuName = input("Pls,Enter Menu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
sumPrice()


