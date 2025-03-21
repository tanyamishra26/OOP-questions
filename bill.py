class Bill:
    def __init__(self,amount):
        self.amount=amount
    def pay_bill(self):
        pass
class Cheque(Bill):
    def __init__(self, amount,check_no):
        super().__init__(amount)
        self.check_no=check_no
    def pay_bill(self):
        return f"amount {self.amount} is paid by cheque having cheque number{self.check_no}"
    
class Cash(Bill):
    def __init__(self, amount):
        super().__init__(amount)

    def pay_bill(self):
        return f"anount {self.amount} is paid by Cash"

# Pay by cheque
cheque_payment = Cheque(5000, "CHK12345")
print(cheque_payment.pay_bill())

 # Pay by cash
cash_payment = Cash(3000)
cash_payment.pay_bill()
    

        