from file_helpers.text_file import get_file_contents, format_list_for_display

products_menu_text = """
    PRODUCTS MENU
    
    0. Return to main menu
    1. Show all products
    2. Create new product
    3. Update existing product
    4. Delete existing product
"""

def products_menu():
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