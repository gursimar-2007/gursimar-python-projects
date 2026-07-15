def sum(x,y):
    sum = x+y
    return sum

x = int(input("Enter x"))
y = int(input("Enter y"))
op = input("Enter op")
match op:
    case '+': print("Sum:",sum(x,y))