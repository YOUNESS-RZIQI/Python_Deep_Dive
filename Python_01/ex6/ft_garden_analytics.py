
class Plant:
    """
    class whith get_info & grow Methods & Atribuits:(name, height
    ,type)
    """

    def __init__(self, name: str, height: int) -> None:
        """Initialize plant with name , height & type"""
        self.name = name
        self.height = height
        self.type = "regular"

    def grow(self) -> None:
        """Increase height by 1cm."""
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """Return plant description."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    class whith get_info Method & Atribuits:(color, is_blooming
    ,type)
    """
    def __init__(self, name: str, height: int, color: str, is_blooming: bool):
        """
        Initialize color , is_blooming & type
        , and pass atribuits to super class
        """
        super().__init__(name, height)
        self.color = color
        self.is_blooming = is_blooming
        self.type = "flowering"

    def get_info(self) -> str:
        """Return flowering plant description."""
        blooming_state = "blooming"
        if self.is_blooming is False:
            blooming_state = "not blooming"
        return super().get_info()+f", {self.color} flowers ({blooming_state})"


class PrizeFlower(FloweringPlant):
    """
    class whith get_info Method & points , type Atribuit.
    """
    def __init__(self, name: str, height: int, color: str, is_blooming: bool,
                 points: int) -> None:
        """
        Initialize PrizeFlower pointes & type
        & pass atribuits to super class
        """
        super().__init__(name, height, color, is_blooming)
        self.points = points
        self.type = "prize"

    def get_info(self) -> str:
        """Return prize flower description."""
        return super().get_info() + f" , Prize points: {self.points}"


class GardenManager:
    """
    Manages a single garden and provides analytics.
    - Tracks plants (self.plants)
    - Uses nested GardenStats to compute statistics (divide & conquer)
    """

    _total_gardens = 0

    class GardenStats:
        """
        Nested helper class for garden statistics.
        - It receives a list of plants and computes analytics.
        """

        def __init__(self, plants) -> None:
            """
            initialize GardenStats plants atribuit
            """
            self.plants = plants

        def count_by_type(self):
            """
            Count plants by their `type` attribute.
            Returns: (regular_count, flowering_count, prize_count)
            """
            regular = 0
            flowering = 0
            prize = 0

            for p in self.plants:
                if p.type == "prize":
                    prize += 1
                elif p.type == "flowering":
                    flowering += 1
                else:
                    regular += 1

            return regular, flowering, prize

        def calculate_score(self) -> int:
            """
              score = sum of heights + for each prize flower add points + BONUS
            """
            score = 0
            for plant in self.plants:
                score += plant.height
                if plant.type == "prize":
                    score += plant.points
                    score += 30

            return score

    def __init__(self, owner: str) -> None:
        """
        Initialize GardenManager atribuits
        (owner, plants, total_growth)
        and add to totol_gardens 1 eache time a
        garden Managwer is created
        """
        self.owner = owner
        self.plants = []
        self.total_growth = 0
        GardenManager._total_gardens += 1

    def add_plant(self, plant, silent=False) -> None:
        """
        Add a plant to this garden.
        """
        self.plants += [plant]
        if not silent:
            print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        """
        Make every plant grow by calling their grow() method.
        """
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def generate_report(self) -> None:
        """
        Print a garden report.
        """
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        plant_count = 0
        for p in self.plants:
            print(f"- {p.get_info()}")
            plant_count += 1

        stats = self.GardenStats(self.plants)
        regular, flowering, prize = stats.count_by_type()

        print()
        print(f"Plants added: {plant_count}, Total growth: "
              f"{self.total_growth}cm")
        print(f"Plant types: {regular} regular, {flowering} flowering,"
              f" {prize} prize flowers")

    @classmethod
    def create_garden_network(cls, garden1, garden2) -> None:
        """
        Compare two gardens' scores.
        """
        score1 = cls.GardenStats(garden1.plants).calculate_score()
        score2 = cls.GardenStats(garden2.plants).calculate_score()
        print(f"Garden scores - {garden1.owner}: {score1}, "
              f"{garden2.owner}: {score2}")
        print(f"Total gardens managed: {cls._total_gardens}")

    @staticmethod
    def validate_height(height) -> bool:
        """
        Returns True if the height is a positive number
        else return False
        """
        return height > 0


print("=== Garden Management System Demo ===")
print()

alice = GardenManager("Alice")
alice.add_plant(Plant("Oak Tree", 100))
alice.add_plant(FloweringPlant("Rose", 25, "red", True))
alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", True, 10))
print()

alice.grow_all()
print()

alice.generate_report()
print()

print(f"Height validation test: {GardenManager.validate_height(10)}")

bob = GardenManager("Bob")
bob.add_plant(Plant("Rose", 92), True)

GardenManager.create_garden_network(alice, bob)
