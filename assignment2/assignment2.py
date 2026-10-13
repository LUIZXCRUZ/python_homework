import csv 
import os 
import custom_module
from datetime import datetime 

def read_employees():
    employee_data = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as file: 
            reader = csv.reader(file) 

            for index, row in enumerate(reader):
                if index == 0: 
                    employee_data["fields"] = row 
                else: 
                    rows.append(row)

        employee_data["rows"] = rows
        return employee_data 

    except Exception as e: 
        print(f"An exception occured: {type(e).__name__}: {e}")
        raise 

employees = read_employees()
print(employees)

def column_index(column_name): #First we create a function that will accept and return the index of a column name 
    return employees["fields"].index(column_name) #employees["fields"] is a list of the column names, so we can use the index() method to find the index of the column name passed in as an argument.

employee_id_column = column_index("employee_id") #Stored the index of the employee id column in a variable called employee_id_column. This will be used later to find the employee id of a specific employee.

print("Employee ID Column: ", employee_id_column)

def first_name(row_number): 
    first_name_column = column_index("first_name")

    row = employees["rows"][row_number]

    return row[first_name_column]

def employee_find (employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

def employee_find_2(employee_id):
    matches = list(filter(
        lambda row: int(row[employee_id_column]) == employee_id, 
        employees["rows"]
    ))
    return matches

def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(
        key=lambda row: row[last_name_column])

    return employees["rows"]

sort_by_last_name()

print(employees)

def employee_dict(row):
    employee_info = {}

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee_info[field] = row[index]

    return employee_info 

def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees

print(all_employees_dict())

def get_this_value():
    return os.getenv("THISVALUE")

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Water is healthy!")

print(custom_module.secret)

def read_minutes():
    minutes1 = {}
    minutes2 = {}
    
    try: 
        with open("../csv/minutes1.csv", "r") as file1: 
            reader1 = csv.reader(file1)

            for index, row in enumerate(reader1):
                if index == 0: 
                    minutes1["fields"] = row 
                else: 
                    minutes1.setdefault("rows", []).append(tuple(row))

        with open("../csv/minutes2.csv", "r") as file2:
            reader2 = csv.reader(file2)

            for index, row in enumerate(reader2):
                if index == 0: 
                    minutes2["fields"] = row 
                else: 
                    minutes2.setdefault("rows", []).append(tuple(row))
    except Exception as e: 
        print(f"An exception occured: {e}")
        raise

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

def create_minutes_set(): 

    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    combined_set = set1.union(set2)

    return combined_set

minutes_set = create_minutes_set()

print("Number of unique records:", len(minutes_set))

def create_minutes_list():
    converted_list = list (
        map(
            lambda row: (
                row[0],
                datetime.strptime(row[1], "%B %d, %Y") 
            ),
            minutes_set
        )
    )
    return converted_list

minutes_list = create_minutes_list()

def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    sorted_minutes = list(
        map(
            lambda row: (
                row[0],
                row[1].strftime("%B %d, %Y")
            ),
            minutes_list
        )
    )

    with(open("./minutes.csv", "w", newline="")) as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(sorted_minutes)

    return sorted_minutes

write_sorted_list()