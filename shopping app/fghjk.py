def sum(x,y):
    sum = x+y
    return sum

def subtract(x,y):
    subtract = x-y
    return subtract

def multiply(x,y):
    multiply = x*y
    return 
x = int(input("Enter x"))
y = int(input("Enter y"))
op = input("Enter op")
match op:
    case '+': print("Sum:",sum(x,y))
    case '-': print("Subtract:",subtract(x,y))
    case '*': print("Multiply:",multiply(x,y))
    case '/': print("Divide:",divide(x,y))