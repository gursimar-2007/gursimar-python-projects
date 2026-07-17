class inventory:
    def __init__(self):
        self.beers={
            1: {"name":"CORONA EXTRA","quantity":100,"price":199},
            2: {"name":"KINGFISHER ULTRA","quantity":109,"price":299},
            3: {"name":"TUBORG CLASSIC","quantity":400,"price":399},
            4: {"name":"BUDWIESER","quantity":70,"price":499},
            5: {"name":"MINTY JAMUN","quantity":200,"price":599}
        }
        self.budget=100000
        self.cart={}
    def displayitems(self):
        print(r"""
        __________________
       /==================\
      |====================|__
      |====================|  )
      |====================|  )
      |====================|__/
      |====================|
      |====================|
      |====================|
      |====================|
      |____________________|
        """)
        self.displayitems
if __name__ == "__main__":
    mall = ()
    mall.start_shopping()