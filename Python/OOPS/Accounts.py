class Account:
    def __init__(self,balance,acc):
        self.balance=balance
        self.account=acc

    def credit(self,amt):
        self.balance+=amt
        print("Enter amt to be credited",amt)
        print(self.balance)

    def debit(self,amt):
        self.balance-=amt
        print("Enter amt to be debited",amt)
        print(self.balance)

    def bal(self):
        return(self.balance)

acc1=Account(100000,1234)
acc1.credit(1000)
acc1.debit(100)

  