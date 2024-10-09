def safe_divide(numerator, denominator):
    try:
        return int(numerator) / int(denominator)
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    except ValueError:
        print("Error: Please enter numeric values only.")