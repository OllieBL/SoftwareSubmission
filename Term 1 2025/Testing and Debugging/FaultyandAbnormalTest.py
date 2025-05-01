def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input, numbers required"

# TODO: Write test cases for abnormal and faulty inputs

print(divide_numbers(2, 0))
print(divide_numbers("2", 4))