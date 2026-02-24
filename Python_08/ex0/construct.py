#!/usr/bin/env python3

import sys
import os
import site


def is_virtual_environment() -> bool:
    """
    Detect if the program is running inside a virtual environment.
    """
    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:
    """
    Return the virtual environment folder name.
    """
    return os.path.basename(sys.prefix)


def show_environment_info() -> None:
    """
    Display information about the current Python environment.
    """
    try:
        print(f"Current Python: {sys.executable}")

        if is_virtual_environment():
            print(f"Virtual Environment: {get_venv_name()}")
            print(f"Environment Path: {sys.prefix}")

            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.\n")

            print("Package installation path:")
            for path in site.getsitepackages():
                print(path)

        else:
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")

            print("Global package installation path:")
            for path in site.getsitepackages():
                print(path)

            print("\nTo enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate  # On Unix")
            print("matrix_env\\Scripts\\activate   # On Windows")

    except Exception as error:
        print(f"Error detecting environment: {error}")


def main() -> None:
    """
    Main program entry.
    """
    if is_virtual_environment():
        print("MATRIX STATUS: Welcome to the construct\n")
    else:
        print("MATRIX STATUS: You're still plugged in\n")

    show_environment_info()


if __name__ == "__main__":
    main()