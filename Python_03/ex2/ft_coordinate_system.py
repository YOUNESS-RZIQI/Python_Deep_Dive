def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:

    """
    Creat a Tuple from (x, y, z)
    """

    return (x, y, z)


def calculate_distance(pos1: tuple[int, int, int],
                       pos2: tuple[int, int, int]) -> float:

    """
    Claculat distance between two positions & return it
    """

    dx: int = pos2[0] - pos1[0]
    dy: int = pos2[1] - pos1[1]
    dz: int = pos2[2] - pos1[2]
    return (dx**2 + dy**2 + dz**2)**(1 / 2)


def parse_coordinates(coord_string: str) -> tuple[int, int, int]:

    """
    Split 3 coordinate and convert them to int then
    call create_position to return them as Tuple of intigers
    """

    args: list[str, str, str] = coord_string.split(',', 3)
    return create_position(int(args[0]), int(args[1]), int(args[2]))


def ft_coordinate_system() -> None:

    """
    Print Coordinate system program.
    """

    try:
        print("=== Game Coordinate System ===\n")
        created_position_1 = create_position(10, 20, 5)
        default_position = create_position(0, 0, 0)

        print("Position created:", created_position_1)
        distance = calculate_distance(default_position, created_position_1)

        print(f"Distance between {default_position} and {created_position_1}: "
              f"{distance:.2f}\n")
    except Exception as e:
        print(f"Error : {e}")
        print(f"Error details - Type: "
              f"{e.__class__.__name__}, Args: {e.args}\n")

    try:
        coord_str = "3,4,0"
        print(f'Parsing coordinates: "{coord_str}"')
        created_position_2 = parse_coordinates(coord_str)
        print("Parsed position:", created_position_2)
        distance = calculate_distance(default_position, created_position_2)
        print(f"Distance between {default_position}"
              f" and {created_position_2}: {distance:.1f}\n")
    except Exception as e:
        print(f"Error : {e}")
        print(f"Error details - Type: "
              f"{e.__class__.__name__}, Args: {e.args}\n")

    try:
        invalid_position_data = "abc,def,ghi"
        print(f'Parsing invalid coordinates: "{invalid_position_data}"')
        created_position_3 = parse_coordinates(invalid_position_data)
        print("Parsed position:", created_position_3)
        distance = calculate_distance(default_position, created_position_3)
        print(f"Distance between {default_position}"
              f" and {created_position_3}: {distance:.1f}\n")

    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: "
              f"{e.__class__.__name__}, Args: {e.args}\n")

    try:
        print("\nUnpacking demonstration:")
        x, y, z = created_position_2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except Exception as e:
        print(f"Error : {e}")
        print(f"Error details - Type: "
              f"{e.__class__.__name__}, Args: {e.args}\n")


ft_coordinate_system()
