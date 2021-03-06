import pymysql
import os
from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

def connect_to_db():
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    cursor = connection.cursor()
    
    return connection, cursor

def format_db_result_for_display(result, field_names) -> PrettyTable:
    table = PrettyTable()
    table.field_names = field_names
    
    for index, item in enumerate(result):
        table.add_row(item)
    
    return table

def get_table(table_name, custom_sql=None):
    connection, cursor = connect_to_db()
    
    select_all_sql = f"SELECT * FROM {table_name}"

    if custom_sql:
        select_all_sql = custom_sql
    
    cursor.execute(select_all_sql)
    column_names = [item[0] for item in cursor.description]
    result = cursor.fetchall()
    
    connection.close()
    
    return result, column_names

def add_to_table(table_name, item):
    connection, cursor = connect_to_db()
    
    column_names = item.keys()
    values = tuple(item.values())
    
    placeholders = ["%s"] * len(item)
    
    insert_sql = f"INSERT INTO {table_name} ({','.join(column_names)}) VALUES ({','.join(placeholders)})"
    
    cursor.execute(insert_sql, values)
    last_row_id = cursor.lastrowid
    connection.commit()
    connection.close()
    
    return last_row_id

def update_item_in_table(table_name, item_id, item):
    if not item:
        return
    connection, cursor = connect_to_db()
    
    column_names = item.keys()
    values = tuple(item.values())
    set_string = []
    
    for name in column_names:
        set_string.append(f"{name} = %s")
    
    update_sql = f"UPDATE {table_name} SET {','.join(set_string)} WHERE id = {item_id}"
    
    cursor.execute(update_sql, values)
    connection.commit()
    connection.close()
    
def delete_items_by_field(table_name, field_name, value):
    connection, cursor = connect_to_db()
    
    delete_sql = f"DELETE FROM {table_name} WHERE {field_name} = %s"
    
    cursor.execute(delete_sql, value)
    connection.commit()
    connection.close()