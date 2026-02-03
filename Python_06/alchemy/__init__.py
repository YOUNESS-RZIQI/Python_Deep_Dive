try:

    __version__ = "1.0.0"
    __author__ = "Master Pythonicus"
    from .elements import create_fire, create_water
    __all__ = ["create_fire", "create_water"]

except Exception as e:
    print("Error: in alchemy/__init__")
    print("The Error is:", e)
