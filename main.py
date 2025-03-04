def main_menu():
    order_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    exchangable_items = ["BAG", "CAP", "TEE", "HOODIE", "JEANS"]
    
    print("~~~~~~~~~~~~~~~\n1. Return\n2. Exchange\n3. Exit\n~~~~~~~~~~~~~~~")
    option = int(input("Please input what you would like to do: "))
    
    if option == 1:
        try:
            order_number = int(input("Input your order number: "))
            if order_number in order_list:
                print("Your request has been processed.")
            else:
                print("Not a valid order number")
        except ValueError:
            print("Please enter a valid number for the order number.")
    
    elif option == 2:
        print(f"List of exchangable items:\n{exchangable_items}")
        item = input("Input what you would like to exchange: ").upper()
        
        if item in exchangable_items:
            print(f"Your {item} has been exchanged for a new one!")
        else:
            print(f"Your {item} isn't available to exchange.")
    
    elif option == 3:
        print("Exiting the service.")
        return False
    return True


loop = True

print("Hello, welcome to customer service")

while loop:
    loop = main_menu()

print("Have a nice day!")