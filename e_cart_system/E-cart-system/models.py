from termcolor import colored
from datetime import datetime
from history_json import save_cart
from playsound import playsound
from pathlib import Path

class user:
    def __init__(self,name):
        if not name.strip():
            self.name = "Guest User"
        else:
            self.name = name.capitalize()
            
        
class CartSys:
    
    def __init__(self):
        self.cart = []
        
    def add_item(self, item_name, quantity, price):
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
        
    
    def cart_print(self, user_name):
        
        print("-"*60,colored("\nPrinting the Cart Details:", "magenta"))
        
        base_dir = Path(__file__).resolve().parent
        
        folder = base_dir / f"Saved Files/Printed Receipts-{datetime.now().strftime('%d-%m-%Y')}"
        folder.mkdir(parents=True, exist_ok=True)
        
        with open(folder / f"cart_details_{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.txt","w",encoding="utf-8") as f:
            
            f.write("="*35+"\n")
            f.write(f"|{" "*10}E-NEXAMART RECEIPT{" "*7}|\n")
            f.write("="*35+"\n")
            f.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            f.write(f"User: {user_name}\n")
            f.write("-"*35+"\n")
            f.write(f"{'Product':<20} {'Qty':<5} {'Price':<10}\n")
            f.write("-"*35+"\n")
            
            for item in self.cart:
                f.write(f"{item[0]:<20} {item[1]:<5} ₹{item[2]:<10}\n")
            
            f.write("="*35+"\n")
            f.write(f"GRAND TOTAL:    ₹{self.total_price():.2f}\n")
            f.write("="*35)
           
        print(colored("Cart details have been printed Successfully to the file.","green"),"\n","-"*60)
        
        
def Sound(audio):
    
    BASE_DIR = Path(__file__).resolve().parent
    AUDIO_DIR = BASE_DIR / "audio"
    file_name = f'{audio}.mp3'
    playsound(str(AUDIO_DIR / file_name))