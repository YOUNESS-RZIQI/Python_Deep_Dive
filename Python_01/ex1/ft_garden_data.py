class Plant:
    """class that store plants data, (name, height, age)"""
    def __init__(self, name: str, height: int, age: int) -> None:
        """inichialize plant name, height and age"""
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        """Print Plant info (name, height in cm, age in days)"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Print plants card info."""
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print("=== Garden Plant Registry ===")
    rose.print_info()
    sunflower.print_info()
    cactus.print_info()


main()
