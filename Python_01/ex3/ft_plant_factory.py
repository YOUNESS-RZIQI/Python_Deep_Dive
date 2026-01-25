class Plant:
    """Store plant data: name, height, age."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """Create plants and display them."""
    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]
    created_plants = 0

    print("=== Plant Factory Output ===")

    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, "
              f"{plant.age} days)")
        created_plants += 1

    print(f"\nTotal plants created: {created_plants}")


main()
