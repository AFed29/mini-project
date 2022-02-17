from menus.products_menu import products_menu
from menus.couriers_menu import couriers_menu
from menus.orders_menu import orders_menu

main_menu_text = """
    MAIN MENU
    
    0. Exit App
    1. Products Menu
    2. Couriers Menu
    3. Orders Menu
"""

print("Welcome to your friendly cafe app!")

def main_menu():
    while True:
        print(main_menu_text)
        main_menu_input = int(input("Please make a choice from above: "))
        
        # Print error message when invalid number is selected
        if main_menu_input not in [0, 1, 2]:
            print('PLEASE ENTER A VALID CHOICE')
        
        # Exit app
        if main_menu_input == 0:
            print("Goodbye!")
            break
        
        # Enter Products Menu
        if main_menu_input == 1:
            products_menu()
        
        # Enter Couriers Menu 
        if main_menu_input == 2:
            couriers_menu()
                        
        # Enter orders menu
        if main_menu_input == 3:
            orders_menu()

