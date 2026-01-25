def check_temperature(temp_str):
    """
    Validates and cleans agricultural temperature data.
    """

    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")

        return None

    try:
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        elif temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

        return temp
    except ValueError as rs_obj:
        print(f"Error: {rs_obj}")
        return None


def test_temperature_input():
    """Simulate different temperature sinarios"""
    try:
        print("=== Garden Temperature Checker ===\n")

        inputs = ["25", "abc", "100", "-50"]

        for tempr in inputs:
            print(f"Testing temperature: {tempr}")
            result = check_temperature(tempr)
            if result is not None:
                print(f"Temperature {result}°C is perfect for plants!")
            print()

        print("All tests completed - program didn't crash!")
    except Exception as rs_obj:
        print(rs_obj)


test_temperature_input()
