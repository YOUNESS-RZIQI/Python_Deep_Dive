try:
    import alchemy
    from .elements import create_air, create_earth

    def healing_potion() -> str:
        return (f"Healing potion brewed with "
                f"{alchemy.elements.create_fire()} and "
                f"{alchemy.elements.create_water()}")

    def strength_potion() -> str:
        return (f"Strength potion brewed with "
                f"{create_earth()} and {alchemy.elements.create_fire()}")

    def invisibility_potion() -> str:
        return (f"Invisibility potion brewed with "
                f"{create_air} and {alchemy.elements.create_water()}")

    def wisdom_potion() -> str:
        return ("Wisdom potion brewed with all elements:" +
                alchemy.elements.create_fire() +
                alchemy.elements.create_water() +
                create_earth() + create_air())

except Exception as e:
    print("Error: in alchemy/potions")
    print("The Error is:", e)
