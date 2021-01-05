try:
    input1 = int(input("A:  "))
    input2 = int(input("b:  "))
    print(input1/input2)
except ValueError :
    print("Error ! Pls, Re-enter")
except ZeroDivisionError :
    print("error !")
except:
    print("Error")