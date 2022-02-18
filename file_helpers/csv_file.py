import csv
from typing import List, Dict, Any
from prettytable import PrettyTable

def get_file_contents(file_name: str) -> List[Dict[str, Any]]:
    with open(file_name, 'r', newline='') as open_file:
        reader = csv.DictReader(open_file)
        file_contents = list(reader)
        
        return file_contents
    
def format_list_for_display(input_list: List[Dict[str, Any]]) -> PrettyTable:
    table = PrettyTable()
    table.field_names = input_list[0].keys()
    
    for index, item in enumerate(input_list):
        table.add_row(item.values())
    
    table.add_autoindex()

    return table

def append_to_csv(file_name: str, item: Dict[str, Any]):
    with open(file_name, 'r', newline='') as open_file:
        reader = csv.DictReader(open_file)
        field_names = reader.fieldnames
    with open(file_name, 'a', newline='') as open_file:        
        writer = csv.DictWriter(open_file, field_names)
        writer.writerow(item)
        
def write_to_csv(file_name: str, items: List[Dict[str, Any]]):
    with open(file_name, 'r', newline='') as open_file:
        reader = csv.DictReader(open_file)
        field_names = reader.fieldnames
    with open(file_name, 'w', newline='') as open_file:        
        writer = csv.DictWriter(open_file, field_names)
        writer.writeheader()
        writer.writerows(items)