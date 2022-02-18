from file_helpers.csv_file import get_file_contents, format_list_for_display, append_to_csv

couriers_menu_text = """
    COURIERS MENU
    
    0. Return to main menu
    1. Show all couriers
    2. Create new courier
"""

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
            print("Couriers List:")
            
            couriers = get_file_contents('data/couriers.csv')
            print(format_list_for_display(couriers))  
        
        # Add new courier
        elif couriers_menu_input == 2:  
            new_courier_name = input("Please enter the name of a new courier: ")
            new_courier_phone_number= input("Please enter the phone number for the new courier: ")
            new_courier = {
                'name': new_courier_name,
                'phone_number': new_courier_phone_number
            }
            
            append_to_csv('data/couriers.csv', new_courier)