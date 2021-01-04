def vatCalculate(totalPrice):
    return totalPrice+(totalPrice*7/100)

price = int(input("Product Price : "))
print("Inc Vat: ", vatCalculate(price))