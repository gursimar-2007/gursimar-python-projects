class restro:
    def __init__(self):
        self.cart={}
        self.food_categories={
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
    # foods = list(food_categories["pizza"].items())
    # items={
    #     "pizza":250,
    #     "burger":140,
    #     "momo":100,
    #     "wraps":140
    # }
    def display_menu(self):
        print("="*60)
        print(f"{"A-LA-CARTE":<60}: {"PRICE":<60}")
        for categories,food in self.food_categories.items():

            print(f"{categories}:")
            print("="*60)
            for foods,price in food.items():
                print(f"{foods:<60}: ₹{price:<60}")
        print("="*60)


    def food_cat(self):
        # cart=[]
        while True:
            any_choice=input("what do you wanna eat today")

            if (any_choice=='q'):
                print("thankyou for choosing our restro")
                break
            self.choice=any_choice.lower()    
            if self.choice in self.food_categories:
                print(f"Available {self.choice}s:")
                for i, (item,price) in enumerate(self.food_categories[self.choice].items(), start=1):
                    print(f"{i}. {item} - {price}")
                food_chc=int(input("enter the index number of the food you want to order"))
                print("please enter q to quit whenever you want")
                if (food_chc>i or food_chc<=0):
                    print("please enter a correct index")
                else:
                    items=list(self.food_categories[self.choice].items())
                    item,price=items[food_chc-1]
                    print(f"you selected {item} and the price is {price} and has been added to cart")
                    self.add_to_cart(item, price)

                    # print(food_categories.items())
                    # while True:
                    # cart.append(price)
                    # total=sum(cart)
                    again=input("do you want to order again please enter q to quit or any other key to continue your order or press v for cart or press d to delete something from your cart").lower()            
                    if(again=='q'):
                        print("thankyou for coming to the restro")
                        break
                    elif(again=='v'):
                        self.display_cart()

            else:
                print("sorry we dont have this thing in our menu yet feel free to call the restro to make this")
    def display_cart(self):
        total=0
        print("="*60)
        print("cart")
        for items,details in self.cart.items():
            price=details["price"]
            quantity=details["quantity"]
            subtotal=price*quantity
        print(f"{items}: {quantity} x ₹{price} = ₹{subtotal}")
        
        total += subtotal
        gst=total*0.025
        print("="*60)
        total += 2*gst
        print("="*60)
        print(f"CGST-₹{gst}")
        print(f"SGST-₹{gst}")
        print("="*60)
        print(f"Grand Total: ₹{total}")
    def add_to_cart(self, item, price):
        if item in self.cart:
            self.cart[item]["quantity"] += 1
        else:
            self.cart[item] = {
                "price": price,
                "quantity": 1
            }
    def remove_from_cart(self):
        if not self.cart:
            print("you cart is emptyy")
            return
        self.display_cart()
        item=print("enter the item you want to remove")
        if item in self.cart:
            del self.cart[item]
            print(f"{item} has been removed from the cart")
        else:
            print(f"item not found in cart")
restaurant = restro()

restaurant.display_menu()
restaurant.food_cat()
restaurant.display_cart()
