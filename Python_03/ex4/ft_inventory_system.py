import sys


def parse_inventory(args: list[str]) -> dict[str, int]:

    """
    Parse command line arguments into inventory dictionary safely.
    """

    inventory: dict[str, int] = {}

    for arg in args:
        if ':' not in arg:
            print(f"Skipping invalid arg (missing ':'): {arg}")
            continue

        name, qty_str = arg.split(':', 1)

        if not name:
            print(f"Skipping invalid arg (empty item name): {arg}")
            continue

        try:
            qty: int = int(qty_str)
        except ValueError:
            print(f"Skipping invalid arg (quantity not int): {arg}")
            continue

        if qty < 0:
            print(f"Skipping invalid arg (negative quantity): {arg}")
            continue

        inventory.update({name: inventory.get(name, 0) + qty})

    return inventory


def get_total_items(inventory: dict[str, int]) -> int:

    """
    Calculate total number of items.
    """

    total: int = 0
    for qty in inventory.values():
        total = total + qty
    return total


def sort_by_quantity(inventory: dict[str, int]) -> list[tuple[str, int]]:
    """Sort inventory by quantity in descending order (bubble sort)."""
    items: list[tuple[str, int]] = []

    items = [(item, qty) for item, qty in inventory.items()]

    i = 0
    while i < (len(items)):
        j = i + 1
        while j < len(items):
            if items[i][1] < items[j][1]:
                items[i], items[j] = items[j], items[i]
            j += 1
        i += 1
    return items


def display_inventory(sorted_items: list[tuple[str, int]], total: int) -> None:

    """
    Display current inventory with percentages.
    """

    print("\n=== Current Inventory ===")

    if len(sorted_items) == 0:
        print("(empty)")
        return

    for name, qty in sorted_items:
        percentage: float = 0.0 if total == 0 else ((qty / total) * 100)
        unit: str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit} ({percentage:.1f}%)")


def display_statistics(sorted_items: list[tuple[str, int]]) -> None:

    """
    Display most and least abundant items.
    """

    print("\n=== Inventory Statistics ===")

    if len(sorted_items) == 0:
        print("No items to analyze.")
        return

    if len(sorted_items) == 1:
        print('There is only One item: ' + sorted_items[0][0] + ' (1 unit))')
        return

    most: tuple[str, int] = sorted_items[0]
    least: tuple[str, int] = sorted_items[-1]

    unit: str = "unit" if most[1] == 1 else "units"
    print(f"Most abundant: {most[0]} ({most[1]} {unit})")

    unit: str = "unit" if least[1] == 1 else "units"
    print(f"Least abundant: {least[0]} ({least[1]} {unit})")


def categorize_items(inventory: dict[str, int]) -> dict[str, dict[str, int]]:

    """
    Categorize items into nested dictionaries by abundance.
    """

    categories: dict[str, dict[str, int]] = {
        "abundant": {},
        "moderate": {},
        "scarce": {}
    }

    for item, qty in inventory.items():
        if qty >= 10:
            categories["abundant"][item] = qty
        elif qty >= 5:
            categories["moderate"][item] = qty
        else:
            categories["scarce"][item] = qty

    return categories


def get_restock_list(inventory: dict[str, int]) -> list[str]:

    """
    Get items that need restocking (qty <= 1).
    """

    restock: list[str] = []

    restock = [item for item, qty in inventory.items() if qty <= 1]

    return restock


def display_dict_properties(inventory: dict[str, int]) -> None:

    """
    Demonstrate dictionary properties.
    """

    print("\n=== Dictionary Properties Demo ===")

    keys_list = [item for item in inventory.keys()]

    values_list = [qty for qty in inventory.values()]

    print("Dictionary keys:", keys_list)
    print("Dictionary values:", values_list)

    has_sword: bool = inventory.get("sword") is not None
    print(f"Sample lookup - 'sword' in inventory: {has_sword}")


def ft_inventory_system() -> None:

    """
    Main function to run inventory system.
    """

    inventory: dict[str, int] = {}
    total: int = 0
    sorted_items: list[tuple[str, int]] = []

    try:
        print("=== Inventory System Analysis ===")

        inventory = parse_inventory(sys.argv[1:])

        if len(inventory) == 0:
            print("No valid inventory items provided.")
            print("Usage example: python3 ",
                  "ft_inventory_system.py sword:3 shield:5")
            return
        total = get_total_items(inventory)
        sorted_items = sort_by_quantity(inventory)

        print("Total items in inventory:", total)
        print("Unique item types:", len(inventory))
    except Exception as e:
        print("Error : ", e)

    try:
        display_inventory(sorted_items, total)
    except Exception as e:
        print("Error : ", e)

    try:

        display_statistics(sorted_items)
    except Exception as e:
        print("Error : ", e)

    try:
        print("\n=== Item Categories ===")
        categories = categorize_items(inventory)
        if len(categories["abundant"]) > 0:
            print("Abundant:", categories["abundant"])
        if len(categories["moderate"]) > 0:
            print("Moderate:", categories["moderate"])
        if len(categories["scarce"]) > 0:
            print("Scarce:", categories["scarce"])

    except Exception as e:
        print("Error : ", e)

    try:
        print("\n=== Management Suggestions ===")
        restock: list[str] = get_restock_list(inventory)
        print("Restock needed:", restock)
    except Exception as e:
        print("Error : ", e)

    try:
        display_dict_properties(inventory)
    except Exception as e:
        print("Error : ", e)


ft_inventory_system()
