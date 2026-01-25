class Plant:
    """Store plant data: name, height, age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name, height, and age."""
        self.plant_name = name
        self.plant_height = height
        self.plant_age = age

    def grow(self) -> None:
        """Increase plant height by 6 cm."""
        self.plant_height += 6

    def age(self) -> None:
        """Increase plant age by 6 days."""
        self.plant_age += 6

    def get_info(self) -> None:
        """Print plant info: name, height in cm, age in days."""
        print(f"{self.plant_name}: {self.plant_height}cm, "
              f"{self.plant_age} days old")


def main() -> None:
    """Simulate plant growth over one week."""
    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 15, 50),
              Plant("Sakora", 150, 204)]

    for plant in plants:
        print("=== Day 1 ===")
        old_plt_height = plant.plant_height

        plant.get_info()

        plant.age()
        plant.grow()

        print(f"=== Day {7} ===")
        plant.get_info()
        print(f"Growth this week: +{plant.plant_height - old_plt_height}cm")
        print("")


main()
