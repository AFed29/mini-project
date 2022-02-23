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

couriers_menu_text = """
    COURIERS MENU
    
    0. Return to main menu
    1. Show all couriers
    2. Create new courier
    3. Update existing courier
    4. Delete existing courier
"""

def display_couriers_list():
    print("Couriers List:")
    couriers, column_names = get_table('couriers')
    print(format_db_result_for_display(couriers, column_names))  

def couriers_menu():
    while True:
        # Display couriers menu and take option
        print(couriers_menu_text)
        couriers_menu_input = int(input("Please make a choice from above: "))
        
        # Return to main menu
        if couriers_menu_input == 0:
            break
        
        # Display list of couriers
        if couriers_menu_input == 1:
            display_couriers_list()
        
        # Add new courier
        elif couriers_menu_input == 2:  
            new_courier_name = input("Please enter the name of a new courier: ")
            new_courier_phone_number= input("Please enter the phone number for the new courier: ")
            new_courier = {
                'name': new_courier_name,
                'phone_number': new_courier_phone_number
            }
            
            add_to_table('couriers', new_courier)
            
        # Update courier
        elif couriers_menu_input == 3:
            display_couriers_list()
            
            update_courier_id = int(input("Enter the id of the courier to update: "))
            updated_courier_name = input("Please enter the new name: ")
            updated_courier_phone_number= input("Please enter the new phone_number: ")
            
            updated_courier = {}
            
            if updated_courier_name:
                updated_courier['name'] = updated_courier_name
            
            if updated_courier_phone_number:
                updated_courier['phone_number'] = updated_courier_phone_number 

            update_item_in_table('couriers', update_courier_id, updated_courier)
            
            
        # Delete courier
        elif couriers_menu_input == 4:
            couriers = get_file_contents('data/couriers.csv')
            print(format_list_for_display(couriers))
            
            courier_index = int(input('Please choose a courier id to delete: '))
            
            couriers.pop(courier_index - 1)
            
            write_to_csv('data/couriers.csv', couriers)