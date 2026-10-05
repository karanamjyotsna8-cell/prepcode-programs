price1=int(input("enter the price of first product:"))
price2=int(input("enter the price of the second product"))
if price1 < price2:
    print("the first product is cheaper")
elif price1 > price2:
    print("the first product is more expansive")
else:
    print("both products have the same price")
