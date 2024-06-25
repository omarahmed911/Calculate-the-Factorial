def calculate_factorial(number):
    factorial = 1
    
    for i in range(1, number + 1):
        factorial *= i
    
    return factorial

if __name__ == "__main__":
    user_input = input("Enter a number to calculate its factorial: ")
    
    try:

        number = int(user_input)
        
        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            result = calculate_factorial(number)
            
            print(f"The factorial of {number} is {result}.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
