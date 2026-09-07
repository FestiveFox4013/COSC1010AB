def add(a, b):
     return a + b

def subtract(a, b):
     return a - b

def multiply(a, b):
     return a * b

def divide(a, b):
     if b == 0:
          return "Error (can not divide by zero)"
     return a / b

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

print ("\nSelect an operation:")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
     print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
     print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
     print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
     print(num1, "/", num2, "=", divide(num1, num2))
else:
     print("Invalid input")
