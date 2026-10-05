#In this code, I will be updating the function of the basic calculator to have more functions and be more like modern calculators.

#This funtion of the code will add two input numbers together.
def add(a, b):
    return a + b

#This function of the code will subtract two input numbers from each other.
def subtract(a, b):
    return a - b

#This function of the code will multiply two input numbers.
def multiply(a, b):
    return a * b

#This function of the code will divide two input numbers. However, if b is equal to zero it will create an error message that states that you can not divide by zero.
def divide(a, b):
    if b == 0:
        return "Error (can not divide by zero)"
    return a / b

OPERATIONS = (
    ("1", "Add", add),
    ("2", "Subtract", subtract),
    ("3", "Multiply", multiply),
    ("4", "Divide", divide)
)

#This piece of code will allow you to store previous calculations.
history = []
#Later imn the code, we will use this to see if the function is 
running = True

while running:
    print("\n--- CALCULATOR SETUP---")
    sets_input = input("How many calculations would you like to use? ")

    if not sets_input.isdigit():
        print("Invalid input. Please enter a whole number, or positive integer.")
        continue

    num_calculations = int(sets_input)

    for i in range(1, num_calculations + 1):

        session_title = f"\n---Calculation {i} of {num_calculations} ---"
        print(session_title)

        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        print("\nSelect an operation:")

        for opt_id, name, symbol in OPERATIONS:
            print(f"{opt_id}. {name}")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            result = add(num1, num2)
            symbol = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == '4':
            result = divide(num1, num2)
            symbol = "/"
        else:
            result = None
            print("Invalid input.")

        if result is not None:
            output = f"{num1} {symbol} {num2} = {result}"
            print(output)

            history.append(output)

        menu_active = True
        while menu_active:
            print("\n--- MENU ---")
            print("1. View History")
            print("2. Run More Calculations")
            print("3. Exit")

            user_action = input("Choose an option (1/2/3): ")
            if user_action == '1':
                print("\n--- Calculation History ---")
                if not history:
                    print("No History Yet.")
                else:
                    for entry in history:
                        print(f"- {entry}")
            elif user_action == '2':
                menu_active = False
            elif user_action == '3':
                menu_active = False
                running = False
                print("Exiting Calculator. Goodbye!")
            else:
                print("Invalid input. Please choose a valid option.")