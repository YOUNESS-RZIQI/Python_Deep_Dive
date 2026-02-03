try:
    from .basic import lead_to_gold
    from ..potions import healing_potion

    def philosophers_stone() -> str:
        return (f"Philosopher’s stone created using {lead_to_gold()} "
                f"and {healing_potion()}")

    def elixir_of_life() -> str:
        return "Elixir of life: eternal youth achieved!"

except Exception as e:
    print("Error: in alchemy/transmutation/advanced")
    print("The Error is:", e)
