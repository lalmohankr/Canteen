menu = {
    'samosa': 20,
    'litti chokha': 40,
    'tea': 10,
    'maggie': 40,
    'paratha': 30,
    'dhokla': 40,
    'water bottle': 20
}

cart = []
total = 0

print("======== Welcome to SAS Canteen ========")

for item, price in menu.items():
    print(f"{item.capitalize()} : {price} Rs.")

while True:
    print("\nMenu: Samosa, Litti chokha, Tea, Maggie, Paratha, Dhokla, Water bottle")
    print("Type 'exit' to finish your order or 'cart' to view your current cart.")

    action = input("What would you like to do? (Add/Remove/Exit/Cart): ").lower()

    if action == "exit":
        print(f"Your final total is {total} Rs. Thank you for visiting SAS Canteen!")
        break

    elif action == "cart":
        if cart:
            print("Items in your cart:")
            for item in cart:
                print(f" - {item.capitalize()}: {menu[item]} Rs.")
            print(f"Total amount: {total} Rs.")
        else:
            print("Your cart is empty.")
        continue

    elif action == "add":
        item = input("Enter the name of the item you want to add: ").lower()
        if item in menu:
            cart.append(item)
            total += menu[item]
            print(f"Your item {item} has been added to your cart successfully.")
        else:
            print(f"Sorry, the item {item} is not available.")

    elif action == "remove":
        item = input("Enter the name of the item you want to remove: ").lower()
        if item in cart:
            cart.remove(item)
            total -= menu[item]
            print(f"Your item {item} has been removed from your cart successfully.")
        else:
            print(f"Sorry, the item {item} is not in your cart.")

    else:
        print("Invalid option. Please choose Add, Remove, Cart, or Exit.")