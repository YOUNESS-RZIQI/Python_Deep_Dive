class GardenError(Exception):
    """Base garden error."""
    pass


class PlantError(GardenError):
    """Plant-related error."""
    pass


class WaterError(GardenError):
    """Watering-related error."""
    pass


def simulate_garden_issues():
    """Demonstrates custom garden errors."""
    print("=== Custom Garden Errors Demo ===\n")

    try:
        try:
            print("Testing PlantError...")
            raise PlantError("The tomato plant is wilting!")
        except PlantError as rs_obj:
            print(f"Caught PlantError: {rs_obj}\n")

        try:
            print("Testing WaterError...")
            raise WaterError("Not enough water in the tank!")
        except WaterError as rs_obj:
            print(f"Caught WaterError: {rs_obj}\n")

        try:
            print("Testing catching all garden errors...")
            raise PlantError("The tomato plant is wilting!")
        except GardenError as rs_obj:
            print(f"Caught a garden error: {rs_obj}")

        try:
            raise WaterError("Not enough water in the tank!")
        except GardenError as rs_obj:
            print(f"Caught a garden error: {rs_obj}\n")

        print("All custom error types work correctly!")
    except Exception as rs_obj:
        print(rs_obj)


simulate_garden_issues()
