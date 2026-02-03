try:
    from .spellbook import record_spell
    from .validator import validate_ingredients

    __all__ = ["record_spell", "validate_ingredients"]
except Exception as e:
    print("Error: in alchemy/grimoire/__init__")
    print("The Error is:", e)
