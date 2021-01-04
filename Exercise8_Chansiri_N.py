username = input("Username : ")
password = input("Password : ")
if username == "Maximus" and password == "Hello":
    print("---Welcome to MustLean มัสลีน---")
    print("1. Tofu Waffle        Price : 55 Bath")
    print("2. Cacao Tofu Waffle  Price : 60 Bath")
    print("3. Noel Ape           Price : 119 Bath")
    print("4. Secret Date        Price : 88 Bath")
    print(" ** Vat Exclude")
    print("Pls, Order by input No.")
else:
    print("Username 0r password incorrect pls try again")
price1 = 55
price2 = 60
price3 = 119
price4 = 88
vat = 7
AddCartItem1 = int(input(">>"))
QytItem1 = int(input("Qyt: "))
if AddCartItem1 == 1:
    print("Tofu Waffle " + str(QytItem1)+ " Qty")
    print("Total Price", str(QytItem1*(price1+(price1*vat/100))) + "THB")
elif AddCartItem1 == 2:
    print("Cacao Tofu Waffle " + str(QytItem1)+ " Qty")
    print("Total Price", str(QytItem1*(price2+(price2*vat/100))) + "THB")
elif AddCartItem1 == 3:
    print("You Order Noel Ape" + str(QytItem1)," Qty")
    print("Total Price", str(QytItem1*(price3+(price3*vat/100))) + "THB")
elif AddCartItem1 == 4:
    print("You Order : Secret Date" + str(QytItem1)+ "Qty")
    print("Total Price", str(QytItem1*(price4+(price4*vat/100))) + "THB")

print("Thank You :)")