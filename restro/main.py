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
items={
    "pizza":250,
    "burger":140,
    "momo":100,
    "wraps":140
}
def display_menu(menu):
    print("="*60)
    for categories,food in menu.items():

        print(f"{categories}")
        for foods in food.items():
            print(f"{foods}")


def food_cat():
    cart=[]
    while True:
        any_choice=input("what do you wanna eat today")

        if (any_choice=='q'):
            print("thankyou for choosing our restro")
            break
        choice=any_choice.lower()    
        if choice in food_categories:
            print(f"Available {choice}s:")
            for i, (item,price) in enumerate(food_categories[choice].items(), start=1):
                print(f"{i}. {item} - {price}")
            food_chc=int(input("enter the index number of your pizza you want to order"))
            print("please enter q to quit whenever you want")
            if (food_chc>i or food_chc<=0):
                print("please enter a correct index")
            else:
                items=list(food_categories[choice].items())
                item,price=items[food_chc-1]
                print(f"you selected {item} and the price is {price} and has been added to cart")
                # print(food_categories.items())
                # while True:
                cart.append(price)
                total=sum(cart)
                again=input("do you want to order again please enter q to quit or any other key to continue your order").lower()            
                if(again=='q'):
                    print("thankyou for coming to the restro")
                    print(total)
                    break

        else:
            print("sorry we dont have this thing in our menu yet feel free to call the restro to make this")

def cart():
    while True:
        food=input("enter a food to buy for yourself and press q to quit")
        if food.lower()=="q":
            print("thank you for purchasing heres your cart")
            break

display_menu(food_categories)
