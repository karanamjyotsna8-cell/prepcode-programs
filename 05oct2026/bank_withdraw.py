balance=int(input("enter the balance"))
amount=5000
if amount<=balance and amount%500==0:
    print("withdraw is allowed")
else:
    print("withdraw not allowed")