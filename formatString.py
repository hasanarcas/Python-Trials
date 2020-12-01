origPrice=float(input("Original Price"))
discount=float(input("Discount as percentage"))
newPrice = (1 - discount/100)* origPrice
calculation = "The original price is {:.2f}$, the discount is {:.2f}% , the final price is {:.2f} $".format(origPrice,discount,newPrice)
print(calculation)




greeting = "Hello, World"
greeting = "J" + greeting[1:]
print(greeting)


