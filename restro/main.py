print("="*60)
items={
    "pizza":250,
    "burger":140,
    "momo":100,
    "wraps":140
}
def food_cat():
    any_choice=input("what do you wanna eat today")
    choice=any_choice.lower()
    food_categories={
        "pizza":{"pepperoni":250,
        "farmhouse":260,
        "pineapple":280,
        "margherita":150
        },
        "burger":{"peri peri veg whopper":140
                  ,"Veg makhani burst":120,
                  "peri peri cheese burger":160
                },
        "wraps":{
            "hot garlic wrap":160,
            "chicken wrap":180,
            "spicy chicken chipotle":130,
            "triple egg wrap":199
            },
        "momos":{"hot steaming":130
                 ,"hot spicy fried":150
                 ,"tandoori momos":120
                }
    }
    if choice in food_categories:
        print(f"Available {choice}s:")
        for i, (item,price) in enumerate(food_categories[choice].items(), start=1):
            print(f"{i}. {item} - {price}")
        food_chc=input("enter the index number of your pizza you want to order")
        items=list(food_categories.items())
        # print(food_categories.items())
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