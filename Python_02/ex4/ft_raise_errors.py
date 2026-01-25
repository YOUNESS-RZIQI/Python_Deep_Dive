def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours}" +
                         " is too low (min 2)")

    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours}" +
                         " is too high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")

    args = [["tomato", 5, 8], ["", 5, 8], ["lettuce", 15, 8], ["rose", 5, 0]]
    counter = 0

    for arg in args:
        try:
            if counter == 0:
                print("Testing good values...")
            if counter == 1:
                print("Testing empty plant name...")
            if counter == 2:
                print("Testing bad water level...")
            if counter == 3:
                print("Testing bad sunlight hours...")

            result = check_plant_health(arg[0], arg[1], arg[2])
            print(result)
        except ValueError as rs_obj:
            print(f"Error: {rs_obj}")
        print("")
        counter += 1

    print("All error raising tests completed!")


test_plant_checks()
