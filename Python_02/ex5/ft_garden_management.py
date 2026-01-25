class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    """
    A GardenManager manage plants, (add, watring, check health)
    """
    def __init__(self):
        self.plants = []
        self.water_tank_level = 2

    def add_plant(self, plant_name):
        """Ensures Integrity: Validates entry before adding to system"""
        try:
            if not plant_name:
                raise ValueError("Plant name cannot be empty!")
            self.plants += [plant_name]
            print(f"Added {plant_name} successfully")
        except ValueError as rs_obj:
            print(f"Error adding plant: {rs_obj}")

    def watering_plants(self, apears=True):
        """Fault Tolerance: Uses finally to ensure system safety"""

        try:
            if apears:
                print("Opening watering system")

            plants_number = 0
            for p in self.plants:
                p = p
                plants_number += 1
            if self.water_tank_level < plants_number:
                raise WaterError("Not enough water in tank")

            for plant in self.plants:
                print(f"Watering {plant} - success")
                self.water_tank_level -= 1

        except WaterError as rs_obj:
            print(f"Caught GardenError: {rs_obj}")
            print("System recovered and continuing...")

        finally:
            if apears:
                print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        if water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 1)")
        elif water_level > 10:
            raise PlantError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours}"
                             f" is too low (min 2)")

        elif sunlight_hours > 12:
            raise PlantError(f"Sunlight hours {sunlight_hours}"
                             f" is too high (max 12)")
        return (f"{plant_name}: healthy (water: {water_level},"
                f" sun: {sunlight_hours})")


def main():
    print("=== Garden Management System ===")
    manager = GardenManager()
    try:
        print("\nAdding plants to garden...")
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except Exception as rs_obj:
        print(rs_obj)

    try:
        print("\nWatering plants...")
        manager.watering_plants()
    except Exception as rs_obj:
        print(rs_obj)

    print("\nChecking plant health...")
    args = [["tomato", 5, 8], ["lettuce", 15, 8]]
    try:
        for arg in args:
            result = manager.check_plant_health(arg[0], arg[1], arg[2])
            print(result)
    except PlantError as rs_obj:
        print(f"Error checking {arg[0]} : {rs_obj}")

    try:
        print("\nTesting error recovery...")
        manager.plants += ["carot"]
        manager.watering_plants(False)
    except WaterError as rs_obj:
        print(f"Caught GardenError: {rs_obj}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


main()
