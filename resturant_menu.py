class Menu:
    
    def __init__(self):
        self.menu ={
            "Burger": 50000,
            "Pizza": 100000,
            "Pasta": 120000,
            "Salad": 60000,
            "Soup": 50000,
            "Coca": 15000,
            }
        self.orders = {}


    

    def display_menu(self):
        print("Menu: ")
        for item,price in self.menu.items():
            print(f"{item}:{price}")

    
    
    

    def take_order(self):
        while True:
            item = input("enter your order (or press q to quit): ")
            if item == "q":
                break
            elif item in self.menu:
                quantity = int(input("enter the quantity: "))
                self.orders[item] = self.orders.get(item, 0) + quantity
            else:
                print("Wrong item! Please select from the menu.")



    

    def calculate_orders(self):
        total = 0
        print("orders: ")
        for item,quantity in self.orders.items():
            price = self.menu[item]
            item_total = price * quantity
            print(f"{item} x {quantity}: {item_total}T")
            total += item_total
        print(f"total: {total}")




menu = Menu()
menu.display_menu()
menu.take_order()
menu.calculate_orders()