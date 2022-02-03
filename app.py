from typing import List

main_menu_text = """
    MAIN MENU
    
    0. Exit App
    1. Products Menu
    2. Couriers Menu
"""
products_menu_text = """
    PRODUCTS MENU
    
    0. Return to main menu
    1. Show all products
    2. Create new product
    3. Update existing product
"""

couriers_menu_text = """
    COURIERS MENU
    
    0. Return to main menu
    1. Show all couriers
    2. Create new courier
"""

def get_file_contents(file_name: str) -> List[str]:
    with open(file_name, 'r') as open_file:
        file_contents = open_file.readlines()
        
        return file_contents
    
def format_list_for_display(input_list):
    display_string = ""
    for index, item in enumerate(input_list):
        display_string += f'{index}. {item.rstrip()}\n'

    return display_string

print("Welcome to your friendly cafe app!")

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
        while True:
            print(products_menu_text)
            products_menu_input = int(input("Please make a choice from above: "))
            
            if products_menu_input == 0:
                break
            
            if products_menu_input == 1:
                print("Products List:")
                
                products = get_file_contents('products.txt')
                print(format_list_for_display(products))     
            
            elif products_menu_input == 2:  
                new_product_input = input("Please enter a new product: ")
                with open('products.txt', 'a') as open_file:
                    open_file.write(new_product_input + '\n')
            
            # Update product
            elif products_menu_input == 3:
                products = get_file_contents('products.txt')
                print(format_list_for_display(products))
                
                product_index = int(input('Please choose a product index to update: '))
                product_name = input('Please choose a new product name: ')
                
                products[product_index] = product_name + '\n'
                
                with open('products.txt', 'w') as file:
                    file.writelines(products)
                
            # Delete Product
            elif products_menu_input == 4:
                products = get_file_contents('products.txt')
                print(format_list_for_display(products))
                
                product_index = int(input('Please choose a product index to delete: '))
                
                products.pop(product_index)
                
                with open('products.txt', 'w') as file:
                    file.writelines(products)
    
    # Enter Couriers Menu 
    if main_menu_input == 2:
        while True:
            print(couriers_menu_text)
            couriers_menu_input = int(input("Please make a choice from above: "))
            
            if couriers_menu_input == 0:
                break
            
            if couriers_menu_input == 1:
                print("Couriers List:")
                
                couriers = get_file_contents('couriers.txt')
                print(format_list_for_display(couriers))  
            
            elif couriers_menu_input == 2:  
                new_courier_input = input("Please enter a new courier: ")
                with open('couriers.txt', 'a') as open_file:
                    open_file.write(new_courier_input + '\n')
