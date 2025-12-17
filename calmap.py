class Calculator:
    def take(self):
        operations = {
            "1": lambda a, b: a + b,
            "2": lambda a, b: a - b if a > b else b - a,
            "3": lambda a, b: a * b,
            "4": lambda a, b: a / b if b != 0 else "Error: Division by zero is not possible."
        }

        while True:
            ch = input("1 for add, 2 for sub, 3 for mult, 4 for div, 5 for exit: ")
            if ch == "5":
                print("Exiting the calculator. Goodbye!")
                break

            if ch in operations:
                try:
                    nums = list(map(float, input("Enter two numbers separated by space: ").split()))
                    if len(nums) != 2:
                        print("Error: Please enter exactly two numbers.")
                        continue
                    result = operations[ch](*nums)
                    print(f"Result: {result}")
                except ValueError:
                    print("Invalid input! Please enter numerical values.")
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid choice! Please select a valid option.")

# Create an object of the Calculator class
cal = Calculator()
cal.take()