def validate_ingredients(ingredients: str) -> str:
    allowed = {"fire", "water", "earth", "air"}
    items = ingredients.split()

    if items and all(item in allowed for item in items):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
