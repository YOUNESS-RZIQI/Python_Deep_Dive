class SecurePlant:
    """
    Represents a plant with secure access to its attributes.
    Height and age can only be modified through validated setter methods.
    """

    def __init__(self, name: str, height: int, age: int):
        """
        Initialize a SecurePlant instance.
        """
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: int):
        """
        Update the plant's height if the value is valid (>= 0).
        """
        if new_height < 0:
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")

    def get_height(self):
        """
        Return the current height of the plant.
        """
        return self._height

    def set_age(self, new_age: int):
        """
        Update the plant's age if the value is valid (>= 0).
        """
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} "
                  f"days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")

    def get_age(self):
        """
        Return the current age of the plant.
        """
        return self._age


def main():
    """
    Demonstrate secure modification of a plant's age and height.
    """
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 20, 26)
    print(f"Plant created: {rose.name}")

    rose.set_height(25)
    rose.set_age(30)

    print("\n")
    rose.set_height(-5)

    print("")
    print(f"Current plant : {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


main()
