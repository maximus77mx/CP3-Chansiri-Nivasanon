def login():
    username = input("Username : ")
    password = input("Password : ")
    if username == "admin" and password == "1234":
        return showMenu()
    else:
        print("User or Password incorrect Pls, Try again!!!")
        return login()
def showMenu():
    print("-----MustLean----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()
def menuSelect():
    UserInput = int(input("Select:  "))
    if UserInput == 1:
        return vatCalculate(int(input("Price(THB):  ")))
    elif UserInput == 2:
        return priceCaculate()
    else:
        print("Try Again !!!")
        return menuSelect()
def vatCalculate(price):
    vat = 7
    result = int(price) + (int(price) * vat / 100)
    return result
def priceCaculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1 + price2)

print("---Welcome to MustLean Shop---")
print("Pls, Log in")
print(login())
print("---THX :)----")
