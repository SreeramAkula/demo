# import random

# choices = ['rock', 'paper', 'scissors']
# user_score = 0
# computer_score = 0

# try:
#     rounds = int(input("How many times do you want to play? "))
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
#     exit()

# for _ in range(rounds):
#     user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

#     if user_choice not in choices:
#         print("Invalid input. Please choose rock, paper, or scissors.")
#         continue

#     computer_choice = random.choice(choices)
#     print(f"Computer chose: {computer_choice}")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (
#         (user_choice == 'rock' and computer_choice == 'scissors') or
#         (user_choice == 'paper' and computer_choice == 'rock') or
#         (user_choice == 'scissors' and computer_choice == 'paper')
#     ):
#         print("You win!")
#         user_score += 1
#     else:
#         print("You lose!")
#         computer_score += 1

# print("\nGame Over!")
# print(f"Your score: {user_score}")
# print(f"Computer's score: {computer_score}")



# vehicle_list = []

# while True:
#     print("\n1. Vehicle Entry\n2. Vehicle Exit\n3. Exit System")
#     choice = int(input("Enter your choice (1/2/3): "))

#     if choice == 1:
#         vehiclenum = input("Enter vehicle number: ")
#         duration = float(input("Enter parking duration: "))
#         entrytime = float(input("Enter entry time: "))

#         vehicle_list.append((vehiclenum, duration, entrytime))
#         print("Vehicle parked successfully!")

#     elif choice == 2:
#         vehiclenum = input("Enter vehicle number for exit: ")
#         exit_time = float(input("Enter exit time: "))

#         for vehicle in vehicle_list:
#             parkedvehiclenum, parkedduration, parkedentrytime = vehicle

#             if parkedvehiclenum == vehiclenum:
#                 actual_duration = exit_time - parkedentrytime
#                 extra_duration = max(0, actual_duration - parkedduration)

#                 total_fee = 50.0 + (10.0 * parkedduration) + (10.0 * extra_duration)
#                 print(f"Total parking fee: Rupees{total_fee}")

#                 vehicle_list.remove(vehicle)
#                 print("Vehicle exited successfully!")
#                 break

#         else:
#             print("Vehicle not found in the system.")

#     elif choice == 3:
#         print("Exiting Vehicle Management System. Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please enter 1, 2, or 3.")





# products = [
#     {'id': 1001, 'name': "Apple", 'price': 1.50, 'quantity': 100},
#     {'id': 1002, 'name': "Banana", 'price': 0.90, 'quantity': 150},
#     {'id': 1003, 'name': "Orange", 'price': 1.20, 'quantity': 80},
#     {'id': 1004, 'name': "Milk", 'price': 2.50, 'quantity': 50},
#     {'id': 1005, 'name': "Bread", 'price': 1.80, 'quantity': 40}
# ]

# while True:
#     print("============ Supermarket Menu ============")
#     print("1. Display products")
#     print("2. Buy product")
#     print("3. Sell product")
#     print("4. Search product by ID")
#     print("5. Search product by Name")
#     print("6. Exit")
#     print("==========================================")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Product ID | Product Name | Price | Quantity")
#         print("---------------------------------------------")
#         for product in products:
#             print(f"{product['id']:10d} | {product['name']:<14s} | {product['price']:>5.2f} | {product['quantity']:>8d}")
    
#     elif choice == 2:
#         id = int(input("Enter the product ID: "))
#         index = -1
#         for i, product in enumerate(products):
#             if product['id'] == id:
#                 index = i
#                 break
#         if index == -1:
#             print("Product not found.")
#         else:
#             quantity = int(input("Enter the quantity: "))
#             if quantity > products[index]['quantity']:
#                 print("Not enough quantity available.")
#             else:
#                 products[index]['quantity'] -= quantity
#                 print("Product purchased successfully.")
    
#     elif choice == 3:
#         id = int(input("Enter the product ID: "))
#         index = -1
#         for i, product in enumerate(products):
#             if product['id'] == id:
#                 index = i
#                 break
#         if index == -1:
#             print("Product not found.")
#         else:
#             quantity = int(input("Enter the quantity: "))
#             products[index]['quantity'] += quantity
#             print("Product sold successfully.")

#     elif choice == 4:
#         id = int(input("Enter the product ID: "))
#         index = -1
#         for i, product in enumerate(products):
#             if product['id'] == id:
#                 index = i
#                 break
#         if index == -1:
#             print("Product not found.")
#         else:
#             product = products[index]
#             print(f"Product ID: {product['id']}")
#             print(f"Product Name: {product['name']}")
#             print(f"Price: {product['price']:.2f}")
#             print(f"Quantity: {product['quantity']}")

#     elif choice == 5:
#         name = input("Enter the product name: ")
#         found = False
#         for product in products:
#             if product['name'].lower() == name.lower():
#                 print(f"Product ID: {product['id']}")
#                 print(f"Product Name: {product['name']}")
#                 print(f"Price: {product['price']:.2f}")
#                 print(f"Quantity: {product['quantity']}")
#                 found = True
#                 break
#         if not found:
#             print("Product not found.")

#     elif choice == 6:
#         print("Thank you for using our supermarket system.")
#         break
    
#     else:
#         print("Invalid choice. Please try again.")







def display_products(products):
    print("Product ID | Product Name | Price | Quantity")
    print("---------------------------------------------")
    for product in products:
        print(f"{product['id']:10d} | {product['name']:<14s} | {product['price']:>5.2f} | {product['quantity']:>8d}")

def buy_product(products):
    id = int(input("Enter the product ID: "))
    index = -1
    for i, product in enumerate(products):
        if product['id'] == id:
            index = i
            break
    if index == -1:
        print("Product not found.")
    else:
        quantity = int(input("Enter the quantity: "))
        if quantity > products[index]['quantity']:
            print("Not enough quantity available.")
        else:
            products[index]['quantity'] -= quantity
            print("Product purchased successfully.")

def sell_product(products):
    id = int(input("Enter the product ID: "))
    index = -1
    for i, product in enumerate(products):
        if product['id'] == id:
            index = i
            break
    if index == -1:
        print("Product not found.")
    else:
        quantity = int(input("Enter the quantity: "))
        products[index]['quantity'] += quantity
        print("Product sold successfully.")

def search_product_by_id(products):
    id = int(input("Enter the product ID: "))
    index = -1
    for i, product in enumerate(products):
        if product['id'] == id:
            index = i
            break
    if index == -1:
        print("Product not found.")
    else:
        product = products[index]
        print(f"Product ID: {product['id']}")
        print(f"Product Name: {product['name']}")
        print(f"Price: {product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")

def search_product_by_name(products):
    name = input("Enter the product name: ")
    found = False
    for product in products:
        if product['name'].lower() == name.lower():
            print(f"Product ID: {product['id']}")
            print(f"Product Name: {product['name']}")
            print(f"Price: {product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")
            found = True
            break
    if not found:
        print("Product not found.")

def main():
    products = [
        {'id': 1001, 'name': "Apple", 'price': 1.50, 'quantity': 100},
        {'id': 1002, 'name': "Banana", 'price': 0.90, 'quantity': 150},
        {'id': 1003, 'name': "Orange", 'price': 1.20, 'quantity': 80},
        {'id': 1004, 'name': "Milk", 'price': 2.50, 'quantity': 50},
        {'id': 1005, 'name': "Bread", 'price': 1.80, 'quantity': 40}
    ]

    while True:
        print("============ Supermarket Menu ============")
        print("1. Display products")
        print("2. Buy product")
        print("3. Sell product")
        print("4. Search product by ID")
        print("5. Search product by Name")
        print("6. Exit")
        print("==========================================")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_products(products)
        elif choice == 2:
            buy_product(products)
        elif choice == 3:
            sell_product(products)
        elif choice == 4:
            search_product_by_id(products)
        elif choice == 5:
            search_product_by_name(products)
        elif choice == 6:
            print("Thank you for using our supermarket system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()