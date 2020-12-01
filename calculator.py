def addition(x,y):
    add = x + y
    return add
def multiplication(x,y):
    mult = x * y
    return mult
def subtraction(x,y):
    sub = x - y
    return sub
def division(x,y):
    div = x/y
    return div
while(True):
    decision = input("Please choose your operation (addition , multiplication , division , subtraction) : ")
    print("Please choose two numbers ")
    a = int(input("First Number : "))
    b = int(input("Second Number : "))
    print("Your numbers are "+ str(a) +" and "+str(b))
    if decision == "addition":
        print("Your answer is : " + str(addition(a,b)))
    elif decision == "multiplication":
        print("Your answer is : " + str(multiplication(a,b)))
    elif decision == "subtraction":
        print("Your answer is : " + str(subtraction(a,b)))
    elif decision == "division":
        print("Your answer is : " + str(division(a,b)))
    else:
        print("Please choose an appropriate word...")