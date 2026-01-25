def garden_operations():
    """
    Simulates different IoT failure patterns and handles them.
    """
    print("=== Garden Error Types Demo ===\n")

    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        x = 10 / 0
        print(x)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        f = open('missing.txt')
        print(f)
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        dic = {"temp": 20}
        print(dic["_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    try:
        print("Testing multiple errors together...")
        dic = {"temp": 20}
        print(dic["_plant"])
        y = 10 / 0
        print(y)
        f = open('missing.txt')
        int("abcdef")
    except (ValueError, KeyError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues\n")


def test_error_types():
    """Runs the failure pattern simulation"""
    garden_operations()
    print("\nAll error types tested successfully!")


test_error_types()
