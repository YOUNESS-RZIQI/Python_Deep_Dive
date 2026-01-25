class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flowering plant."""

    def __init__(self, name: str, height: int, age: int, color: str):
        """Initialize flower with color."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display blooming message."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Represents a tree plant."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initialize tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Calculate and display shade produced by the tree."""
        shade_in_m2 = self.trunk_diameter * 1.56
        print(f"{self.name} provides {shade_in_m2:.0f} square meters of shade")


class Vegetable(Plant):
    """Represents a vegetable plant."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        """Initialize vegetable with harvest season and nutrition."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional_value_message(self) -> None:
        """Display nutritional value message."""
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def main() -> None:
    """Run garden plant demonstration."""

    flowers = [Flower("Rose", 25, 30, "red"),
               Flower("Lily", 30, 45, "white")]

    trees = [Tree("Oak", 500, 1825, 50),
             Tree("Maple", 400, 1500, 40)]

    vegetables = [Vegetable("Tomato", 80, 90, "summer", "C"),
                  Vegetable("Carrot", 35, 70, "autumn", "A")]

    print("=== Garden Plant Types ===\n")

    for flower in flowers:
        print(
            f"{flower.name} (Flower): {flower.height}cm, {flower.age} days, "
            f"{flower.color} color"
        )
        flower.bloom()
        print("")

    for tree in trees:
        print(
            f"{tree.name} (Tree): {tree.height}cm, {tree.age} days, "
            f"{tree.trunk_diameter}cm diameter"
        )
        tree.produce_shade()
        print("")

    for vegetable in vegetables:
        print(
            f"{vegetable.name} (Vegetable): {vegetable.height}cm, "
            f"{vegetable.age} days, {vegetable.harvest_season} harvest"
        )
        vegetable.nutritional_value_message()
        print("")


main()
