def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"

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

def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

def repeat(string, count):
    result = ""
    for i in range(count):
        result = result + string
    return result 

def student_scores(mode, **kwargs):
    if mode == "best":
        best_name = ""
        best_score = 0
        for name, score in kwargs.items():
            if score > best_score: 
                best_score = score 
                best_name = name
        return best_name
    elif mode == "mean":
        return sum(kwargs.values())/len(kwargs)
    
def titleize (string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    result = []
    for i, word in enumerate (words):
        if i == 0 or i == len (words) -1 or word not in little_words: 
            result.append(word.capitalize())
        else: 
            result.append(word)    
    return " ".join(result)

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess: 
            result = result + letter
        else: 
            result = result + "_"
    return result 