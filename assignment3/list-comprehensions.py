import csv 

with open("../csv/employees.csv", newline="") as file: 
    reader = csv.reader(file)
    employees = list(reader)

employees_names = [
    row[1] + " " + row[2] 
    for row in employees[1:]
]

print(employees_names)

names_with_e = [
    name for name in employees_names if "e" in name 
]

print(names_with_e)