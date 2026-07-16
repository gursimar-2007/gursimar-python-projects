class ShoppingMall:
    def __init__(self):
        self.items = {
            1: {"name":"SNACKS","quantity":200,"price":80},
            2 :{"name":"BULDAK","quantity":123,"price":200},
            3 :{"name":"COLA","quantity":100,"price":100},
            4 :{"name":"FAST FOOD","quantity":100,"price":120},
            5 :{"name":"BOOZE","quantity":100,"price":700},
        }
        self.balance=3000
        self.cart={}
    def display_items(self):
        print("="*60)
        print("AVAILAIBLE ITEMS")
        print("="*60)
        # print(f"{s_no:self.items})
        print(f"{"S.no":<8} {"name":<20}{"quantity":<20}  {"price":<20}")
        print("-"*60)
        for s_no,item in self.items.items():
            print(f"{s_no:<8} {item['name']:<20} {item['quantity']:<20}  {item["price"]:<20}")
            # print("availaible balance"=="hllo")
            print("-"*60)
        print(f"AVAILAIBLE BALANCE ={self.balance}")
        print("="*60)
    def startShopping(self):
        print("welcome to the SKYDECK")
        self.display_items()
        while True:
            sno=input("enter the serial number")
            if sno=="x":
                print("thank you for shopping at SKYDECK")
                break
            try:
                sno=int(sno)
            except ValueError:
                print("please input a significant number the number you have put is invalid")
                break
            qty=input("HOW MUCH QUANTITY?")
            if qty=="x":
                    print("THANKYOU FOR SHOPPING AT SKYDECK")
            try:
                qty=int(qty)
                if qty<=0:
                    print("please enter a valid quantity number")
            except ValueError:
                print("THE NUMBER OF QUANTITY YOU HAVE PUT IS INVALID PLEASE PROCEED WITH A VALID NUMBER")
            if self.buy_item(sno,qty):
                contd=input.strip.lower("do you want to continue shopping")
                if contd!=y:
                    print("thankyou for shopping at sky deck")
                    break
    def buy_item(self,sno,qty):
        if sno not in self.items:
            print("sno does not exist")
            return False
        item=self.items[sno]
        # print(item)
        if qty>item["quantity"]:
            print("INSUFFICIENT QUANTITY PLEASE COME LATER")
            return False
        total_cost=qty*item["price"]
        item['quantity']-=qty
        self.balance-=total_cost
if __name__=="__main__":

    mall = ShoppingMall()
    mall.startShopping()