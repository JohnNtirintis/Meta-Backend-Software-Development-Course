class WagePayments:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"
    
    def status(self):
        if self.payment == "yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"
        
john = WagePayments("John", "no", 1000)
jorge = WagePayments("Jorge", "no", 1200)

print(john.status(), "\n", jorge.status())

john.pay()
print("After payment")
print(john.status())
