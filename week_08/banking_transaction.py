class InvalidBalanceError(Exception):
    pass
class InvalidWithdrawalError(Exception):
    pass
class InsufficientBalanceError(Exception):
    pass
try:
    bal = int(input("Enter Balance: "))
    withdrawal = int(input("Enter Withdrawal amount: "))
    if bal < 0:
        raise InvalidBalanceError("Invalid Balance")
    if withdrawal < 0:
        raise InvalidWithdrawalError("Invalid Withdrawal")
    if withdrawal > bal:
        raise InsufficientBalanceError("Insufficient Balance")
    print("Success, Balance =", bal - withdrawal)
except ValueError:
    print("Error: Invalid Input")

except (InvalidBalanceError,InvalidWithdrawalError,InsufficientBalanceError) as e:
    print("Error:", e)