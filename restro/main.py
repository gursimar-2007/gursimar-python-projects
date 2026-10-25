print("="*60)

# print the menu here

print("="*60)




def cart():
    while True:
        food=input("enter a food to buy for yourself and press q to quit")
        # food.lower
        if food.lower()=="q":
            print("thank you for purchasing heres your cart")
            # display the cart
            break