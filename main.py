
def main_menu():
    order_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("~~~~~~~~~~~~~~~\n1. Return\n2. Exchange\n3. Exit\n~~~~~~~~~~~~~~~")
    option = int(input("Please input what you would like to do: "))
    if option == 1:
        if(input("Input your order number") in order_list):
            print("Your request has been processed.")
        else:
            print("Not a valid order number")
    elif option == 2:
        print("Doing something cool...2")
    elif option == 3:
        return False


loop = True

print("Hello, welcome to customer service")


while loop:
    loop = main_menu()

print("Have a nice day!")



