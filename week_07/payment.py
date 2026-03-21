from abc import abstractmethod,ABC
class Payment(ABC):
    @abstractmethod
    def validate_payment(self):
        pass
    @abstractmethod
    def process_payment(self,details):
        pass
class CreditCardPayment(Payment):
    def validate_payment(self,details):
        return details.isdigit() and len(details)==16
    def process_payment(self,details):
        if self.validate_payment(details):
            print("Payment Successfull.")
        else:
            print("Error:Invalid Card Number")
class UpiPayment(Payment):
    def validate_payment(self,details):
        return "@" in details
    def process_payment(self,details):
        if self.validate_payment(details):
            print("Payment Successfull.")
        else:
            print("Error:Invalid UPI ID")
if __name__=="__main__":
    while True:
        ch=int(input("1.Make Payment 2.Exit\nEnter Choice :"))
        if ch==2:
            break
        elif ch==1:
            t=input("Enter Type (UPI/CARD)")
            amt=int(input("Enter Amount :"))
            if t.upper()=="UPI":
                id=input("Enter Upi ID")
                new=UpiPayment()
                new.process_payment(id)
            elif t.upper()=="CARD":
                id=input("Enter CARD Details")
                new=CreditCardPayment()
                new.process_payment(id)
        else:
            print("Enter Valid Input ")
