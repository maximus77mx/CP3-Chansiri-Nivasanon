def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

price = int(input("Product Price : "))
print("Inc Vat: ", vatCalculate(price))