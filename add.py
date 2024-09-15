def addNum (num1, num2):
    return num1 + num2

if __name__ == "__main__":
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the sum
        result = addNum(num1, num2)

        # Display the result
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")