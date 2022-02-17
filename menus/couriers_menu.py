from file_helpers.text_file import get_file_contents, format_list_for_display

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
            
            couriers = get_file_contents('data/couriers.txt')
            print(format_list_for_display(couriers))  
        
        # Add new courier
        elif couriers_menu_input == 2:  
            new_courier_input = input("Please enter a new courier: ")
            with open('data/couriers.txt', 'a') as open_file:
                open_file.write(new_courier_input + '\n')