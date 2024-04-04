def add(x,y):
    return x+y
def substitution(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y==0:
        return "undefined"
    return x/y


print("WELCOME TO MY CALCULATOR\n")
while True:
    user_input=input("+ for addition, - for subtitution,* for multiplication,/ for divition, quit to quit the calculator:\n ")

    if user_input.lower()=="quit":
        break


    x=float(input("Enter first number: "))
    y=float(input("Enter second number: "))
    if user_input=="+":
        print("Result: ",add(x,y))
    elif user_input=="-":
        print("Result: ",substitution(x,y))
    elif user_input=="*":
        print("Result: ",multiplication(x,y))
    elif user_input=="/":
        print("Result: ",division(x,y))
    else:
        print("Invalid input try again")


