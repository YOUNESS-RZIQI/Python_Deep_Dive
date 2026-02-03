try:
    from .basic import lead_to_gold, stone_to_gem
    from .advanced import philosophers_stone, elixir_of_life

    __all__ = ["lead_to_gold", "stone_to_gem",
               "philosophers_stone", "elixir_of_life"]
except Exception as e:
    print("Error: in alchemy/transmutation/__init__")
    print("The Error is:", e)
