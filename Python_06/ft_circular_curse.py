try:
    from alchemy.grimoire import record_spell, validate_ingredients
    # from alchemy.grimoire import spellbook
    # from alchemy.grimoire import validator

    # try:
    #     spellbook.record_spell("", validator.validate_ingredients)
    # except Exception:
    #     print("", end="")

    print("\n=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print('validate_ingredients("fire air"):',
          validate_ingredients("fire air"))
    print('validate_ingredients("dragon scales"):',
          validate_ingredients("dragon scales"))

    print("\nTesting spell recording with validation:")
    print('record_spell("Fireball", "fire air"):',
          record_spell("Fireball", "fire air"))
    print('record_spell("Dark Magic", "shadow"):',
          record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    import alchemy.grimoire.spellbook as obj
    print('record_spell("Lightning", "air"):',
          obj.record_spell("Lightning", "air"))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
except Exception as e:
    print("Error: in ft_circular_curse")
    print("Error:", e)
