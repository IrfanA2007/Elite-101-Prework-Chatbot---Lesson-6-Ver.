
def main_menu():
    print("~~~~~~~~~~~~~~~\n1. Placeholder\n2. Placeholder\n3.Placeholder\n4. Exit Chatbot\n~~~~~~~~~~~~~~~")
    option = int(input("Please input what you would like to do: "))
    if option == 1:
        print("Doing something cool...1")
    elif option == 2:
        print("Doing something cool...2")
    elif option == 3:
        print("Doing something cool...3")
    if option == 4:
        return False
    else:
        return True


loop = True

print("Hello, welcome to the chatbot interface!")

name = input("Please input your name: ")
age = input(f"Hello {name}, please input your age: ")


while loop:
    loop = main_menu()

print("Thank you for using the chatbot!")



