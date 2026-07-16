class shopping_mall :
    def __init__(self):
        self.items = {
            1:{"name":"beverages","quantity":200,"price":70},
            2:{"name":"Diary Products","quantity":70,"price":100},
            3:{"name":"stationary","quantity":300,"price":50},
            4:{"name":"fruits","quantity":200,"price":30},
            5:{"name":"vegetable","quantity":100,"price":20}
        }
        self.balance = 3000
        self.cart = {}
    def display_items(self):
        
        print("=" * 60)
        print("AVAILABLE ITEMS")
        print("="*60)
        print(f"{'S.No':<6} {'items':<15} {'quantity':<15} {'price'}")
        print("-"*60)
        for s_no, item in self.items.items():
            print(f"{s_no:<6} {item['name']:<15} {item['quantity']:<15} {item['price']}")
        print('='* 60)   
        print(f"your current balance :{self.balance} ") 
        print("=" *60)
    def buy_item(self,s_no,quantity):
        if s_no not in self.items :
            print("s_no doesnot exit")
            return False
        item = self.items[s_no]
        if quantity > item['quantity']:
            print("insufficient stock") 
            return False
        total_cost = quantity*item['price']
        if total_cost > self.balance:
            print("insufficient balance")
            return False

        item['quantity']-= quantity
        self.balance -= total_cost
        

        if s_no in self.cart:
            self.cart[s_no]['quantity']+=quantity
        else:
            self.cart[s_no]= {"name": item['name'],
            "quantity": quantity,
            "price": item["price"],
            "total":total_cost}
        print(self.display_items())
        return True     
    def display_cart(self):
        if not self.cart:
            print("\n your cart is empty .")
            return
        print("=" * 60)
        print("AVAILABLE ITEMS")
        print("="*60)
        print(f"{'S.No':<6} {'items':<15} {'quantity':<15} {'price'}")
        print("-"*60)
        for s_no, item in self.items.items():
            print(f"{s_no:<6} {item['name']:<15} {item['quantity']:<15} {item['price']}")
        print('='* 60)   
        print(f"your current balance : Rs. {self.balance} ") 
        print("=" *60)
        

        
    def start_shopping(self):
        print("welcome to my shopping mall!")
        print("you have Rs.3000 to spend.")
        print("Enter x to exit at anytime.")
        self.display_items()
        while True:
            s_no = input("Enter serial no of item to buy ")
            if s_no == 'x':
                break

            try :
                s_no = int(s_no)
            except ValueError:
                print("enter a valid number")

            quantity = input("Enter quantity of item to buy")
            if quantity == 'x':
                break 
            
            try:
                quantity = int(quantity)
                if quantity <=0 :
                    print("enter a positive number")
            except ValueError:
                print("enter a valid number")

            if self.buy_item(s_no,quantity):
                continue_shopping = input("do you want to continue shopping").strip().lower()
                if continue_shopping !='y':
                    break
        self.display_cart()
        print("\n thank you for shopping with us")


if __name__=="__main__":
    mall = shopping_mall()
    mall.start_shopping()