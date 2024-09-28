import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(expression: str) -> float:
    try:
        operand1, operator_symbol, operand2 = expression.split()
        operand1, operand2 = float(operand1), float(operand2)

        if operator_symbol not in operations:
            raise ValueError(f"Unsupported operator: {operator_symbol}")

        result = operations[operator_symbol](operand1, operand2)
        return result
    
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero is not allowed.")
    except ValueError as ve:
        raise ValueError(f"Invalid input: {ve}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def user_interface():
    print("Welcome to the Text-Based Calculator!")
    print("Enter your expression in the format: operand1 operator operand2")
    print("Supported operators: +, -, *, /")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        user_input = input("\nEnter your expression: ")
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        try:
            result = calculate(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    user_interface()
