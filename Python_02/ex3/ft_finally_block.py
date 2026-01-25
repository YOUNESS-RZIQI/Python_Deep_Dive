def water_plants(plant_list: list):
    """
    Waters plants safely
    """
    try:
        print("Opening watering system")

        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")

    except Exception as rs_obj:
        print(f"Error: {rs_obj}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Runs watering tests with normal and error scenarios.
    """
    try:
        print("=== Garden Watering System ===\n")
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully!")

        print("\nTesting with error...")
        water_plants(["tomato", None, "carrots"])
    except Exception as rs_obj:
        print(rs_obj)


test_watering_system()
