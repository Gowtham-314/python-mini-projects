import json
from datetime import datetime
from pathlib import Path

def save_cart(cart, username):
        
    base_dir = Path(__file__).resolve().parent
        
    folder = base_dir / "Saved Files/Cart History"
    folder.mkdir(parents=True, exist_ok=True)

    filename = folder / f"cart_history-{datetime.now().strftime('%d-%m-%Y')}.json"

    # Load or initialize file
    if filename.exists():
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = {}

    # Create user section if not exists
    if username not in data:
        data[username] = []

    # Prepare cart entry
    cart_entry = {
        "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": [],
        "grand_total": 0
    }

    total = 0
    for item in cart:
        item_total = item[1] * item[2]
        total += item_total

        cart_entry["items"].append({
            "item_name": item[0],
            "quantity": item[1],
            "price": item[2],
            "total": item_total
        })

    cart_entry["grand_total"] = total

    # Save cart under that user
    data[username].append(cart_entry)

    # Write back to file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)