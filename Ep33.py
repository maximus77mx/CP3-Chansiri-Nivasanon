'''
คำนวนภาษีมูลค่าเพิ่ม
'''
price = input("ราคาสินค้า :   " )
vat = 7
result = int(price)+(int(price)*vat/100)
print(result)