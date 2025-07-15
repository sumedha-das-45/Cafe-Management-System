# Cafe Management System

menu = {
    1: {"name": "Coffee", "price": 50},
    2: {"name": "Tea", "price": 30},
    3: {"name": "Sandwich", "price": 80},
    4: {"name": "Burger", "price": 120},
    5: {"name": "Pasta", "price": 150},
    6: {"name": "Pizza", "price": 250}
}

order = {}

def display_menu():
    print("\n====== Café Menu ======")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ₹{item['price']}")
    print("========================\n")

def take_order():
    while True:
        try:
            item_id = int(input("Enter item number to order (0 to finish): "))
            if item_id == 0:
                break
            if item_id not in menu:
                print("❌ Invalid item. Try again.")
                continue
            qty = int(input(f"Enter quantity for {menu[item_id]['name']}: "))
            if item_id in order:
                order[item_id]["quantity"] += qty
            else:
                order[item_id] = {"name": menu[item_id]["name"], "price": menu[item_id]["price"], "quantity": qty}
        except ValueError:
            print("❌ Invalid input. Enter numbers only.")

def display_bill():
    print("\n======= 🧾 Order Summary =======")
    total = 0
    for item in order.values():
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"{item['name']} x {item['quantity']} = ₹{item_total}")
    print(f"\nTotal Amount: ₹{total}")
    print("Thank you for visiting our café! ☕")
    print("===============================")

# Main program
print("Welcome to Python Café!")
display_menu()
take_order()
if order:
    display_bill()
else:
    print("No items ordered. Goodbye!")
