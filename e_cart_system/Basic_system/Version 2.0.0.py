'''<!--- E-Commerce Cart System
    This program allows users to add items to a shopping cart, view the cart contents,
    Systemed by Kruthik BT , Gowtham Gowda  C B , Akash B V , Rohith S J  
    @Coding_group--->'''


from termcolor import colored
from datetime import datetime
import sys
import os

# Enable UTF-8 encoding for Windows console
if sys.platform == "win32":
    os.system("chcp 65001 > nul")
    sys.stdout.reconfigure(encoding="utf-8")

class E_cart_system():
    
    def __init__(self):
        print("\n","-"*60,colored(f"\n|{" "*18}E-Commerce Cart System {" "*18}|\n", "red", attrs=["bold"]),"-"*60)
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
        print("\n","-"*60)
        print(colored("\nViewing the Items in the Cart:\n", "blue"))
        print(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n")
        print("-" * 40)
        for item in self.cart: 
            print(f"{item[0]:<20} {item[1]:<5} ₹{item[2]:.2f}\n")
        print("-" * 60)
        print(colored("Calculating the Total Price of the Items in the Cart:", "yellow"))
        print(f"\nTotal Price: ₹ {self.total_price()}")
        print("-"*60)
        
    def cart_print(self):
        print("-"*60)
        print(colored("Printing the Cart Details:", "magenta"))
        with open(f"cart_details_{datetime.now().strftime('%D%m%Y%H%M%S')}.txt","w",encoding="utf-8") as f:
            f.write("="*35+"\n")
            f.write(f"|{" "*8}E-COMMERCE RECEIPT{" "*7}|\n")
            f.write("="*35+"\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"User: {self.name}\n")
            f.write("-"*35+"\n")
            f.write(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n")
            f.write("-"*35+"\n")
            for item in self.cart:
                f.write(f"{item[0]:<20} {item[1]:<5} ₹{item[2]:<10}\n")
            f.write("="*35+"\n")
            f.write(f"GRAND TOTAL:    ₹{self.total_price():.2f}\n")
            f.write("="*35+"\n")
            
        print(colored("Cart details have been printed Successfully to the file.","green"),"\n","-"*60)
        
if __name__ == "__main__":
    cart_sys = E_cart_system()
    cart_sys.user_details(input("Enter your name: ").capitalize())
    print("\n","-"*60,colored(f"\nWelcome to E-Commerce Cart System ,{cart_sys.name}!", "cyan", attrs=["bold"]),"\n","-"*60)

    while True:
        print(colored("\nChoice the Actions to perform:", "green", attrs=["bold"]))
        print(colored('''1. Add Item to Cart\n2. View Cart Items\n3. Print Cart Details\n4. Exit''', "green"))
        choice = int(input(colored("Enter your choice: ", "cyan")))
        if not choice in [1,2,3,4]:
            print(colored("Invalid choice. Please try again.", "red"),"\n","-"*60)
            continue
        match choice:
            case 1:
                no_items = int(input("\nEnter the No. of items to add: "))
                for _ in range(no_items):
                    item_name, quantity, price = input("Enter item name, quantity, and price (separated by commas): ").split(',')
                    if not quantity.isdigit() or not price.isdigit():
                        quantity,price = 0,0
                    cart_sys.add_item(item_name, int(quantity), float(price))
                    
            case 2:
                if cart_sys.cart:
                    cart_sys.view_cart()
                else:
                    print(colored("Your cart is empty. Please Choice 1 to add Items.", "red", attrs=["bold"]))
                    continue
            case 3:
                if cart_sys.cart:
                    cart_sys.cart_print()
                else:
                    print(colored("Your cart is empty. Please Choice 1 to add Items.", "red", attrs=["bold"]))
                    continue
            case 4:
                print(colored("\nExiting the E-Commerce Cart System. Thank you!", "red", attrs=["bold"]))
                break