from file_helpers.csv_file import (
    get_file_contents,
    format_list_for_display,
    append_to_csv,
    write_to_csv)
from db.db_helper import (
    get_table,
    format_db_result_for_display,
    add_to_table)

orders_menu_text = """
    ORDERS MENU
    
    0. Return to main menu
    1. Show all Orders
    2. Create new order
    3. Update order status
    4. Update entire order
    5. Delete order
"""

def update_order_status(order_number, new_status):
    orders = get_file_contents('data/orders.csv')
    orders[order_number - 1]['status'] = new_status
    
    write_to_csv('data/orders.csv', orders)

def orders_menu():
    while True:
        print(orders_menu_text)
        orders_menu_input = int(input("Please make a choice from above: "))
        
        # Return to main menu
        if orders_menu_input == 0:
            break
        
        # Display list of orders
        if orders_menu_input == 1:
            print("orders List:")
            join = "SELECT orders.id, customer_name, customer_address, customer_phone,\
                couriers.name AS `courier name`, status GROUP_CONCAT(products.name) AS products \
                FROM orders \
                JOIN products_on_orders ON orders.id=order_id \
                JOIN couriers ON courier_id=couriers.id \
                JOIN products ON product_id=products.id \
                GROUP BY orders.id"
            orders, column_names = get_table('orders', join)
            print(format_db_result_for_display(orders, column_names))  
        
        # Add new order
        elif orders_menu_input == 2:  
            customer_name = input("Please enter a customer name: ")
            customer_address = input("Please enter a customer address: ")
            customer_phone = input("Please enter a customer phone number: ")
            
            print("Couriers List:")
            couriers, column_names = get_table('couriers')
            print(format_db_result_for_display(couriers, column_names)) 
            
            courier = int(input("Please enter a courier number: "))
            
            new_order ={
                "customer_name": customer_name,
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "courier_id": courier,
                "status": "preparing"
            }
            
            order_id = add_to_table('orders', new_order)
            
            print("Products List:")
            products, column_names = get_table('products')
            print(format_db_result_for_display(products, column_names))
            
            products_for_order = input('Please select the product ids for the order (e.g 1,2,3): ').split(',')
            
            for product_id in products_for_order:
                add_to_table('products_on_orders', {"order_id":order_id, "product_id": int(product_id)})
            
        
        # Update order status
        elif orders_menu_input == 3:
            print("orders List:")
            orders = get_file_contents('data/orders.csv')
            print(format_list_for_display(orders))
                
            order_number = int(input("Please select the order number to update: "))
            new_status = input("Please enter the new status: ")
            
            update_order_status(order_number, new_status)
            
        # Update order
        elif orders_menu_input == 4:
            orders = get_file_contents('data/orders.csv')
            print(format_list_for_display(orders))
            
            update_order_index = int(input('Please choose a order index to update: '))
            
            updated_customer_name = input("Please enter a customer name: ")
            updated_customer_address = input("Please enter a customer address: ")
            updated_customer_phone = input("Please enter a customer phone number: ")
            
            print("Couriers List:")
            couriers = get_file_contents('data/couriers.csv')
            print(format_list_for_display(couriers))
            
            updated_courier = int(input("Please enter a courier number: "))
            updated_status = input("Please enter a status: ")
            
            updated_order = {}
            
            if updated_customer_name:
                updated_order['customer_name'] = updated_customer_name
            
            if updated_customer_address:
                updated_order['customer_address'] = updated_customer_address 
                
            if updated_customer_phone:
                updated_order['customer_phone'] = updated_customer_phone
            
            if updated_courier:
                updated_order['courier'] = updated_courier - 1
                
            if updated_status:
                updated_order['status'] = updated_status 
            
            orders[update_order_index - 1].update(updated_order)
            
            write_to_csv('data/orders.csv', orders)
            
            
        # Delete order
        elif orders_menu_input == 5:
            orders = get_file_contents('data/orders.csv')
            print(format_list_for_display(orders))
            
            order_index = int(input('Please choose a order index to delete: '))
            
            orders.pop(order_index - 1)
            
            write_to_csv('data/orders.csv', orders)