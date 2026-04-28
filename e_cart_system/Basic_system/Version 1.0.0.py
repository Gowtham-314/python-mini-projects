from termcolor import colored
from datetime import datetime

class E_cart_system():
    
    def __init__(self):
        print(colored("\nE-Commerce Cart System\n", "red", attrs=["bold"]))
        self.cart = []
        
        
    def user_details(self, name):
        self.name = name    

    def add_item(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.cart.append([item_name, quantity, price])
        
    def total_price(self):
        total_sum = sum(item[1] * item[2] for item in self.cart)
        return total_sum
        
    def view_cart(self):
        print("\n+"*60)
        print(colored("\nViewing the Items in the Cart:\n", "blue"))
        print(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n")
        print("-" * 40)
        for item in self.cart: 
            print(f"{item[0]:<20} {item[1]:<5} ₹{item[2]:.2f}\n")
        print("-" * 60)
        print(colored("Calculating the Total Price of the Items in the Cart:", "yellow"))
        print(f"\nTotal Price: ₹ {self.total_price()}.00")
        print("="*60)
        
    def cart_print(self):
        print("="*60)
        print(colored("\nPrinting the Cart Details:", "magenta"))
        with open(f"cart_details_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt", "w") as f:
            f.write("================================\n")
            f.write("|       E-COMMERCE RECEIPT       |\n")
            f.write("================================\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"User: {self.name}\n")
            f.write("--------------------------------\n")
            f.write(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n")
            f.write("--------------------------------\n")
            for item in self.cart:
                f.write(f"{item[0]:<20} {item[1]:<5} ₹{item[2]:<10}\n")
            f.write("================================\n")
            f.write(f"GRAND TOTAL:    ₹{self.total_price():.2f}\n")
            f.write("================================\n")
            
        print(colored("\nCart details have been printed Successfully to the file.", "green"))
        
if __name__ == "__main__":
    cart_sys = E_cart_system()
    cart_sys.user_details(input("Enter your name: ").capitalize())
    print(colored(f"\nWelcome to the E-Commerce Cart System ,{cart_sys.name}!\n", "cyan", attrs=["bold"]))

    while True:
        print(colored("Choice the Actions to perform:", "green", attrs=["bold"]))
        print(colored('''1. Add Item to Cart\n2. View Cart Items\n3. Print Cart Details\n4. Exit''', "green"))
        choice = int(input(colored("Enter your choice: ", "cyan")))
        match choice:
            case 1:
                no_items = int(input("\nEnter number of items to add: "))
                for _ in range(no_items):
                    item_name, quantity, price = input("Enter item name, quantity, and price (separated by commas): ").split(',')
                    cart_sys.add_item(item_name, int(quantity), float(price))
                    
            case 2:
                cart_sys.view_cart()
            case 3:
                cart_sys.cart_print()
            case 4:
                print(colored("\nExiting the E-Commerce Cart System. Thank you!", "red", attrs=["bold"]))
                break