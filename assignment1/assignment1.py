def hello():
    return "Hello!"

print(hello())

def greet(name):
    return f"Hello, {name}!"

print(greet("James"))

# def calc(a, b, operation = "multiply"):
#     pass 

#operation = "multiply" is a (default parameter as mentioned in 1.6)
# If the caller leaves it out, it multiplies. 
# Pass becomes a placeholder that doesn't anything quite yet 

def calc(a, b, operation = "multiply"):
    try: 
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b 
        elif operation == "divide":
            return a/b 
        elif operation == "modulo":
            return a % b 
        elif operation == "int_divide":
            return a//b
        elif operation == "power":
            return a ** b 
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

def data_type_conversion(value, type_name):
    try:
        if type_name == "float":
            return float(value)
        elif type_name == "int":
            return int(value)
        elif type_name == "str":
            return str(value)
    except ValueError:
        return f"You can't convert {value} into a {type_name}."

