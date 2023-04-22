# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

# Class Bank
class Bank(ABC):
    # An abstract bank class
    def basicinfo():
        print("This is a generic bank")
        return "Generic bank: 0"
    
    @abstractmethod
    def withdraw():
        pass

# Class Swiss
class Swiss(Bank):
    # A specific type of bank than derives from class Bank
    def __init__(self):
        self.bal = 1000

    def basicinfo(self):
        print("This is the swiss bank")
        return "Swiss Bank: " + str(self.bal)
    
    def withdraw(self, widthrdaw_amount):
        # If balance is lower than the requested withdrawn amount
        # Then print insuffient funds and return the current balance
        if self.bal < widthrdaw_amount:
            print("Insufficient Funds")
            return self.bal
        # Else contiue by deducting the widthrawn amount from the balance
        # and print the transactions and return the new balance
        self.bal -= widthrdaw_amount 
        print(f"Withdrawn amount: {widthrdaw_amount}")
        print(f"New Balance: {self.bal}")
        return self.bal

# Driver Code
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()