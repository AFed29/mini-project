from typing import List

orders = []

main_menu_text = """
    MAIN MENU
    
    0. Exit App
    1. Products Menu
    2. Couriers Menu
    3. Orders Menu
"""
products_menu_text = """
    PRODUCTS MENU
    
    0. Return to main menu
    1. Show all products
    2. Create new product
    3. Update existing product
    4. Delete existing product
"""

couriers_menu_text = """
    COURIERS MENU
    
    0. Return to main menu
    1. Show all couriers
    2. Create new courier
"""

orders_menu_text = """
    ORDERS MENU
    
    0. Return to main menu
    1. Show all Orders
    2. Create new order
    3. Update order status
"""

def get_file_contents(file_name: str) -> List[str]:
    with open(file_name, 'r') as open_file:
        file_contents = open_file.readlines()
        
        return file_contents
    
def format_list_for_display(input_list: List[str]) -> str:
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
            # Display products menu and take option
            print(products_menu_text)
            products_menu_input = int(input("Please make a choice from above: "))
            
            # Return to main menu
            if products_menu_input == 0:
                break
            
            # Display list of products
            if products_menu_input == 1:
                print("Products List:")
                
                products = get_file_contents('data/products.txt')
                print(format_list_for_display(products))     
            
            # Add new product
            elif products_menu_input == 2:  
                new_product_input = input("Please enter a new product: ")
                with open('data/products.txt', 'a') as open_file:
                    open_file.write(new_product_input + '\n')
            
            # Update product
            elif products_menu_input == 3:
                products = get_file_contents('data/products.txt')
                print(format_list_for_display(products))
                
                product_index = int(input('Please choose a product index to update: '))
                product_name = input('Please choose a new product name: ')
                
                products[product_index] = product_name + '\n'
                
                with open('data/products.txt', 'w') as file:
                    file.writelines(products)
                
            # Delete Product
            elif products_menu_input == 4:
                products = get_file_contents('data/products.txt')
                print(format_list_for_display(products))
                
                product_index = int(input('Please choose a product index to delete: '))
                
                products.pop(product_index)
                
                with open('data/products.txt', 'w') as file:
                    file.writelines(products)
    
    # Enter Couriers Menu 
    if main_menu_input == 2:
        while True:
            # Display couriers menu and take option
            print(couriers_menu_text)
            couriers_menu_input = int(input("Please make a choice from above: "))
            
            # Return to main menu
            if couriers_menu_input == 0:
                break
            
            # Display list of couriers
            if couriers_menu_input == 1:
                print("Couriers List:")
                
                couriers = get_file_contents('data/couriers.txt')
                print(format_list_for_display(couriers))  
            
            # Add new courier
            elif couriers_menu_input == 2:  
                new_courier_input = input("Please enter a new courier: ")
                with open('data/couriers.txt', 'a') as open_file:
                    open_file.write(new_courier_input + '\n')
                    
    # Enter orders menu
    if main_menu_input == 3:
        # Display orders menu and take option
        while True:
            print(orders_menu_text)
            orders_menu_input = int(input("Please make a choice from above: "))
            
            # Return to main menu
            if orders_menu_input == 0:
                break
            
            # Display list of orders
            if orders_menu_input == 1:
                print("orders List:")
                for index, order in enumerate(orders):
                    print(order)  
            
            # Add new order
            elif orders_menu_input == 2:  
                customer_name = input("Please enter a customer name: ")
                customer_address = input("Please enter a customer address: ")
                customer_phone = input("Please enter a customer phone number: ")
                
                print("Couriers List:")
                couriers = get_file_contents('data/couriers.txt')
                print(format_list_for_display(couriers))
                
                courier = int(input("Please enter a courier number: "))
                
                orders.append({
                    "customer_name": customer_name,
                    "customer_address": customer_address,
                    "customer_phone": customer_phone,
                    "courier": courier,
                    "status": "preparing"
                })
            
            # Update order status
            elif orders_menu_input == 3:
                print("orders List:")
                for index, order in enumerate(orders):
                    print(index, order)
                    
                order_number = int(input("Please select the order number to update: "))
                new_status = input("Please enter the new status: ")
                
                orders[order_number]['status'] = new_status

