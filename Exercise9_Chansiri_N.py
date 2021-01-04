'''
!= หมายถึง ไม่เท่ากันๅ
'''
username = input("Username : ")
password = input("Password : ")
while username != "Maximus" or password != "Hello":
    print("Username or Password incorrect")
    username = input("Username : ")
    password = input("Password : ")
print("Done")