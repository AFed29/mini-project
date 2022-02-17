from typing import List

def get_file_contents(file_name: str) -> List[str]:
    with open(file_name, 'r') as open_file:
        file_contents = open_file.readlines()
        
        return file_contents
    
def format_list_for_display(input_list: List[str]) -> str:
    display_string = ""
    for index, item in enumerate(input_list):
        display_string += f'{index}. {item.rstrip()}\n'

    return display_string