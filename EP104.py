class Customer:
    Name = ""
    LastName = ""
    Age = 0

    def AddCart(self):
        print("Add productt to",self.Name,self.LastName, "'s cart")

customer1 = Customer()
customer1.Name = "Chansiri"
customer1.LastName = "M"
customer1.AddCart()

customer2 = Customer()
customer2.Name = "Tiny"
customer2.LastName = "L"
customer2.AddCart()

customer3 = Customer()
customer3.Name = "Art"
customer3.LastName = "Lim"
customer3.AddCart()