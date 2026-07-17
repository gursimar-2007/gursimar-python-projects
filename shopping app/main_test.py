class shopping_mall:
    def __init__(self):
        self.items = {
            1: {"name": "beverages", "quantity": 200, "price": 70},
            2: {"name": "Diary Products", "quantity": 70, "price": 100},
            3: {"name": "stationary", "quantity": 300, "price": 50},
            4: {"name": "fruits", "quantity": 200, "price": 30},
            5: {"name": "vegetable", "quantity": 100, "price": 20}
        }
        self.balance = 3000
        self.cart = {}

    def display_items(self):
        print("=" * 60)
        print("AVAILABLE ITEMS")
        print("=" * 60)
        print(f"{'S.No':<6} {'items':<15} {'quantity':<15} {'price'}")
        print("-" * 60)
        for s_no, item in self.items.items():
            print(f"{s_no:<6} {item['name']:<15} {item['quantity']:<15} {item['price']}")
        print('=' * 60)   
        print(f"your current balance : Rs. {self.balance}") 
        print("=" * 60)

    def display_cart(self):
        if not self.cart:
            print("\nyour cart is empty.")
            return

        print("\n" + "=" * 60)
        print("YOUR CURRENT CART")
        print("=" * 60)
        print(f"{'Items':<18} {'Quantity':<15} {'Price':<12} {'Total (Rs.)'}")
        print("-" * 60)
        
        grand_total = 0
        for item in self.cart.values():
            print(f"{item['name']:<18} {item['quantity']:<15} {item['price']:<12} {item['total']}")
            grand_total += item['total']
            
        print('=' * 60)   
        print(f"Total Cart Value:  Rs. {grand_total}")
        print(f"Remaining Balance: Rs. {self.balance}") 
        print("=" * 60)

    def buy_item(self, s_no, quantity):
        if s_no not in self.items:
            print("\ns_no does not exist")
            return False
        item = self.items[s_no]
        if quantity > item['quantity']:
            print("\ninsufficient stock") 
            return False
        total_cost = quantity * item['price']
        if total_cost > self.balance:
            print("\ninsufficient balance")
            return False

        item['quantity'] -= quantity
        self.balance -= total_cost

        if s_no in self.cart:
            self.cart[s_no]['quantity'] += quantity
            self.cart[s_no]['total'] += total_cost
        else:
            self.cart[s_no] = {
                "name": item['name'],
                "quantity": quantity,
                "price": item["price"],
                "total": total_cost
            }
        
        print("\nItem added successfully!")
        # self.display_cart()
        self.display_items()
        return True     
        
    def start_shopping(self):
        print("welcome to my shopping mall!")
        print("you have Rs.3000 to spend.")
        print("Enter x to exit at anytime.")
        self.display_items()
        
        while True:
            s_no = input("\nEnter serial no of item to buy: ").strip()
            if s_no.lower() == 'x':
                break

            try:
                s_no = int(s_no)
            except ValueError:
                print("enter a valid number")
                continue

            quantity = input("Enter quantity of item to buy: ").strip()
            if quantity.lower() == 'x':
                break 
            
            try:
                quantity = int(quantity)
                if quantity <= 0:
                    print("enter a positive number")
                    continue
            except ValueError:
                print("enter a valid number")
                continue

            if self.buy_item(s_no, quantity):
                continue_shopping = input("do you want to continue shopping? (y/n): ").strip().lower()
                if continue_shopping != 'y':
                    break
                    
        self.display_cart()
        print("\nthank you for shopping with us")


if __name__ == "__main__":
    mall = shopping_mall()
    mall.start_shopping()