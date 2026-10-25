print("="*60)
items={
    "pizza":250,
    "burger":140,
    "momo":100,
    "wraps":140
}
def food_cat():
    food_categories={
        "pizza":["pepperoni","farmhouse","pineapple","margherita"],
        "burger":["peri peri veg whopper","Veg makhani burst","peri peri cheese burger"],
        "wraps":["hot garlic wrap","chicken wrap","spicy chicken chipotle","triple egg wrap"],
        "momos":["hot steaming","hot spicy fried","tandoori momos"]
    }

print("="*60)



def food_display():
    pass
def cart():
    while True:
        food=input("enter a food to buy for yourself and press q to quit")
        # food.lower
        if food.lower()=="q":
            print("thank you for purchasing heres your cart")
            # display the cart
            break
    