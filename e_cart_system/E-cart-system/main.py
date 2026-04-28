""""<!--- E-Commerce Cart System
    This program allows users to add items to a shopping cart, view the cart contents,
    Systemed by Kruthik BT , Gowtham Gowda  C B , Akash B V , Rohith S J
    @Coding_group--->"""
    
    
from termcolor import colored,cprint
from models import user, CartSys,Sound
from history_json import save_cart


def E_NexaMart():
    
    
    cart_obj = CartSys()
    user_obj=user(input("\nEnter your Name, (Press Enter ↩ to Guest User) : "))
    print("\n","-"*60,colored(f"\n|{" "*25}{colored('E-NexaMart', "red", attrs=['bold', 'underline'])}{" "*25}|\n", "red", attrs=["bold"]),"-"*60)
    print("\n","-"*60,colored(f"\nWelcome to E-NexaMart ⫸\n{colored(user_obj.name, 'red', attrs=['bold'])}!", "cyan", attrs=["bold"]),"\n","-"*60)

    while True:
        
        print(colored("\nChoice the Actions to perform:", "green", attrs=["bold","underline"]))
        print(colored('''1. Add Item to Cart\n2. View Cart Items\n3. Print Cart Details\n4. Exit''', "green"))
        
        try:
            choice = int(input(colored("Enter your choice: ", "cyan")))
            if not choice in [1,2,3,4]:
                Sound('error')
                cprint("Invalid choice. Please try again.", "white","on_light_red", attrs=["bold"])
                print("\n","-"*60)
                continue
        except ValueError:
            Sound('error')
            cprint("Invalid input. Please enter a number between 1 and 4.", "white","on_light_red", attrs=["bold"])
            print("\n","-"*60)
            continue
        
        
        match choice:
            
            case 1:
            
                had_error = False
                try:
                    no_items = int(input(colored("\nEnter the No. of items to add: ", "light_blue")))
                    
                    if no_items <= 0:
                        raise ValueError
                
                    for _ in range(no_items):
                        try:
                            items, qty, rate = input(colored("Enter item Name, Quantity and Price (Separated by Commas): ", "light_blue")).split(',')
                            qty = int(qty)
                            rate = float(rate)

                            if qty <= 0 or rate <= 0:
                                raise ValueError
                            
                        except ValueError:
                            had_error = True
                            Sound('error')
                            cprint("Invalid item details. Quantity and price must be positive numbers. Enter in the correct format.","white","on_light_red", attrs=["bold"])
                            print("\n","-"*60)
                            break
                            
                        cart_obj.add_item(items, qty, rate)     
                
                except ValueError:
                    Sound('error')
                    cprint("Invalid input. Please enter the valid positive number of items.", "white","on_light_red", attrs=["bold"])
                    print("\n","-"*60)
                    continue
                
                if not had_error:
                    Sound('success')  
                                      
            case 2:
                if cart_obj.cart:
                    cart_obj.view_cart()
                    Sound('success')
                else:
                    Sound('error')
                    cprint("Your cart is empty. Please Choice 1 to add Items.", "white","on_light_red", attrs=["bold"])
                    print("\n","-"*60)
                    continue
            case 3:
                if cart_obj.cart:
                    cart_obj.cart_print(user_obj.name)
                    Sound('success')

                else:
                    Sound('error')
                    cprint("Your cart is empty. Please Choice 1 to add Items.", "white","on_light_red", attrs=["bold"])
                    print("\n","-"*60)
                    continue
            case 4:
                if cart_obj.cart:
                    save_cart(cart_obj.cart, user_obj.name)
                    print(colored("Your cart has been saved to a JSON file before exiting.", "yellow", attrs=["bold"]))
                Sound('success')
                print("\n")
                cprint("Exiting the E-Commerce Cart System. Thank you!", "white","on_light_red", attrs=["bold"])
                print("\n","-"*60)
                break
                    
            case _:
                cprint("Invalid choice. Please try again.", "white","on_light_red", attrs=["bold"])
                print("\n","-"*60)
    

if __name__ == "__main__":
    E_NexaMart()