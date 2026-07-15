def sum():
    sum = a+b
    return sum


outout = sum()
print("sum", outout)

x = int(input("Enter x"))
y = int(input("Enter y"))
op = input("Enter op")
match op:
    case '+': sum(x,y)