class ShoppingMall:
    def __init__(self):
        self.items = {
            1: {"name":"SNACKS","quantity":200,"price":80},
            2 :{"name":"BULDAK","quantity":123,"price":200},
            3 :{"name":"COLA","quantity":100,"price":100},
            4 :{"name":"FAST FOOD","quantity":100,"price":120},
            5 :{"name":"BOOZE","quantity":100,"price":700},
        }
    def display_items(self):
        print("="*60)
        print("AVAILAIBLE ITEMS")
        print("="*60)
        # print(f"{s_no:self.items})
        for s_no,item in self.items.items():
            print(f"{s_no:<8} {item['name']:<20} {item['quantity']:<20}  {item["price"]:<20}")
            print("")
    def startShopping(self):
        print("welcome to the SKYDECK")
        self.display_items()


if __name__=="__main__":
    mall = ShoppingMall()
    mall.startShopping()