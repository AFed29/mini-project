from file_helpers.text_file import get_file_contents, format_list_for_display

orders_menu_text = """
    ORDERS MENU
    
    0. Return to main menu
    1. Show all Orders
    2. Create new order
    3. Update order status
"""

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