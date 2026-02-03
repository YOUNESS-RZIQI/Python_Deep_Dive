try:
    import alchemy.elements

    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")

    print(f"alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")

    print(f"alchemy.elements.create_water():"
          f" {alchemy.elements.create_water()}")

    print(f"alchemy.elements.create_earth():"
          f" {alchemy.elements.create_earth()}")

    print(f"alchemy.elements.create_air():"
          f" {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")

    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    try:
        print(f"Version: {alchemy.__version__}")
    except AttributeError:
        print("__version__ not found.")

    try:
        print(f"Author: {alchemy.__author__}")
    except AttributeError:
        print("__author__ not found.")


except Exception as e:
    print("Error: in ft_sacred_scroll")
    print("Error:", e)
