username = input("Username : ")
password = input("Password : ")
if username == "admin" and password == "1234" :
    print("Done")
    print("-----MustLean----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    UserInput = int(input("____"))
    if UserInput == 1:
        price = input("ราคาสินค้า :   ")
        vat = 7
        result = int(price) + (int(price) * vat / 100)
        print(result)
    elif UserInput == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1+price2)
else:
    print("Username 0r password incorrect pls try again")