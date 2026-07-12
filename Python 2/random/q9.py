# Object‑Oriented Programming  
# Create a class BankAccount with methods to deposit, withdraw, and check_balance.
# Test it with some transactions.

class BankAccount :
    def __init__(self, name, acc, bal):
        self.name = name
        self.acc = acc
        self.bal = bal

    def chk_bal(self) :
        print(f"\nHi {self.name}")
        print("Your Avaiblable Bal : ", self.bal)

    def depo(self, am) : 
        self.bal += am
        print(f"\n{self.name} deposited : {am}")
        print("Avaiblable Bal : ", self.bal)

    def withdr(self, am) :
        self.bal -= am
        print(f"\n{self.name} withdrawn : {am}")
        print("Avaiblable Bal : ", self.bal)

c1 = BankAccount("Gautam", "123", 1000000)
c1.chk_bal()
c1.withdr(200)
c1.depo(10000)
