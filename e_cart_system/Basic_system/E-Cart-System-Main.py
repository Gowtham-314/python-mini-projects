'''<!--- E-Commerce Cart System
    This program allows users to add items to a shopping cart, view the cart contents,
    Systemed by Kruthik BT , Gowtham Gowda  C B , Akash B V , Rohith S J  
    @Coding_group--->'''


from termcolor import colored
from datetime import datetime

class E_cart_system():
    
    def __init__(self,name):
        print("\n","-"*60,colored(f"\n|{" "*18}E-Commerce Cart System {" "*18}|\n", "red", attrs=["bold"]),"-"*60)
        self.cart = []
        if not name.strip():
            self.name = "Guest User"
        else:
            self.name = name.capitalize()
        
    def add_item(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.cart.append([item_name, quantity, price])
        
    def total_price(self):
        total_sum = sum(item[1] * item[2] for item in self.cart)
        return total_sum
        
    def view_cart(self):
        
        print("\n","-"*60,colored("\nViewing the Items in the Cart:\n", "blue"),'-'*40)
        print(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n","-" * 40)
        
        for item in self.cart: 
            print(f"{item[0]:<20} {item[1]:<5} ₹{item[2]:.2f}\n")
            
        print("-" * 60,colored("\nCalculating the Total Price of the Items in the Cart:", "yellow"))
        print(f"\nTotal Price: ₹ {self.total_price()}\n","-"*60)
        
        
    def cart_print(self):
        print("-"*60,colored("\nPrinting the Cart Details:", "magenta"))
        with open(f"cart_details_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt","w",encoding="utf-8") as f:
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
            f.write("="*35)
            
        print(colored("Cart details have been printed Successfully to the file.","green"),"\n","-"*60)
        
if __name__ == "__main__":
    
    cart_sys = E_cart_system(input("\nEnter your Name, (Press Enter ↩ to Guest User) : "))
    print("\n","-"*60,colored(f"\nWelcome to E-Commerce Cart System ⫸\n{colored(cart_sys.name, 'red', attrs=['bold'])}!", "cyan", attrs=["bold"]),"\n","-"*60)

    while True:
        
        print(colored("\nChoice the Actions to perform:", "green", attrs=["bold"]))
        print(colored('''1. Add Item to Cart\n2. View Cart Items\n3. Print Cart Details\n4. Exit''', "green"))
        
        try:
            choice = int(input(colored("Enter your choice: ", "cyan")))
            if not choice in [1,2,3,4]:
                print(colored("Invalid choice. Please try again.", "red"),"\n","-"*60)
                continue
        except ValueError:
            print(colored("Invalid input. Please enter a number between 1 and 4.", "red"),"\n","-"*60)
            continue
        
        
        match choice:
            
            case 1:
            
                try:
                    no_items = int(input("\nEnter the No. of items to add: "))
                    for _ in range(no_items):
                        item_name, quantity, price = input("Enter item Name, Quantity and Price (Separated by Commas): ").split(',')
                        quantity = 0 if not quantity.isdigit() else quantity
                        price = 0 if not price.isdigit() else price
                        cart_sys.add_item(item_name, int(quantity), float(price))
                except ValueError:
                    print(colored("Invalid input format. Please enter the details correctly.", "red"),"\n","-"*60)
                    continue
                    
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
            
            case _:
                print(colored("Invalid choice. Please try again.", "red"),"\n","-"*60)