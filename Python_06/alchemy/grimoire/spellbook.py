try:
    def record_spell(spell_name: str, ingredients: str) -> str:
        from .validator import validate_ingredients
        result = validate_ingredients(ingredients)
        if "INVALID" not in result:
            return f"Spell recorded: {spell_name} ({result})"
        else:
            return f"Spell rejected: {spell_name} ({result})"
except Exception as e:
    print("Error: in alchemy/grimoire/spellbook")
    print("The Error is :", e)
