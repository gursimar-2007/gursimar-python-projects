print("="*60)
items={
    "pizza":250,
    "burger":140,
    "momo":100,
    "wraps":140
}
def food_cat():
    choice=input("what do you wanna eat today")
    food_categories={
        "pizza":["pepperoni","farmhouse","pineapple","margherita"],
        "burger":["peri peri veg whopper","Veg makhani burst","peri peri cheese burger"],
        "wraps":["hot garlic wrap","chicken wrap","spicy chicken chipotle","triple egg wrap"],
        "momos":["hot steaming","hot spicy fried","tandoori momos"]
    }
    print(enumerate[food_categories[choice]])
    if choice in food_categories:
        print(food_categories[choice])
    else:
        print("sorry we dont have this thing in our menu yet feel free to call the restro to make this")
# print("="*60)



# def food_display():
def cart():
    while True:
        food=input("enter a food to buy for yourself and press q to quit")
        # food.lower
        if food.lower()=="q":
            print("thank you for purchasing heres your cart")
            # display the cart
            break
# food_display()
food_cat()