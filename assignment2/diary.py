import traceback #Helps explain the error and where it happened

try: #Attempts to run the code below, if it fails, it will go to the except block
    with open("diary.txt", "a") as file: #Opens the diary file in append mode
        prompt = "What happened today? "
        while True: #Keeps repeating until the user types "done for now"
            entry = input(prompt)

            file.write(entry + "\n") #Saves the entry to the diary file

            if entry.strip().lower() == "done for now": #Checks whether to finish the diary entry
                break #Exits the loop 

            prompt = "What else? "

except Exception as e: 
    print("An exception occured.") #Handles non-fatal errors and prints the exception type, message, and stack trace

    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = []

    for trace in trace_back: 
        stack_trace.append(
            f"File: {trace[0]}, Line: {trace[1]},"
            f"Function: {trace[2]}, Message: {trace[3]}"
        )

    print(f"Exception type: {type(e).__name__}")
    print("Stack trace:")
    for trace in stack_trace:
        print(trace)

    if str(e):
        print(f"Exception message: {e}")