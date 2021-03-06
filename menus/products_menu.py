from file_helpers.csv_file import (
    get_file_contents,
    format_list_for_display,
    append_to_csv,
    write_to_csv)
from db.db_helper import (
    get_table,
    format_db_result_for_display,
    add_to_table,
    update_item_in_table)

products_menu_text = """
    PRODUCTS MENU
    
    0. Return to main menu
    1. Show all products
    2. Create new product
    3. Update existing product
    4. Delete existing product
"""

def display_products_list():
    print("Products List:")
    products, column_names = get_table('products')
    print(format_db_result_for_display(products, column_names))      

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
            display_products_list()
        
        # Add new product
        elif products_menu_input == 2:  
            new_product_name = input("Please enter the name of a new product: ")
            new_product_price= input("Please enter the price of a new product: ")
            new_product = {
                'name': new_product_name,
                'price': new_product_price
            }
            
            add_to_table('products', new_product)
        
        # Update product
        elif products_menu_input == 3:
            display_products_list()
            
            update_product_id = int(input("Enter the id of the product to update: "))
            updated_product_name = input("Please enter the new name: ")
            updated_product_price= input("Please enter the new price: ")
            
            updated_product = {}
            
            if updated_product_name:
                updated_product['name'] = updated_product_name
            
            if updated_product_price:
                updated_product['price'] = updated_product_price 
            
            update_item_in_table('products', update_product_id, updated_product)
            
            
        # Delete Product
        elif products_menu_input == 4:
            display_products_list()
            
            product_index = int(input('Please choose a product id to delete: '))
            
            products.pop(product_index - 1)
            
            write_to_csv('data/products.csv', products)