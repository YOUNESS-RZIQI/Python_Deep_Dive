import sys
import os
import site


def is_virtual_environment() -> bool:

    # Detect if the program is running inside a virtual environment.

    return sys.prefix != sys.base_prefix


def get_venv_name() -> str:

    # Return the virtual environment name.

    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path:
        return os.path.basename(venv_path)
    return "Unknown"


def show_environment_info() -> None:

    # Display information about the current Python environment.

    try:
        print(f"Current Python: {sys.executable}")

        if is_virtual_environment():
            print(f"Virtual Environment: {get_venv_name()}")
            print(f"Environment Path: {sys.prefix}")

            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.\n")

            print("Package installation path:")
            print(site.getsitepackages()[0])

        else:
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")

            print("\nTo enter the construct, run:")
            print("python3 -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate # On Windows")
            print("\nThen run this program again.")

    except Exception as error:
        print(f"Error detecting in show_environment_info(): {error}")


def main() -> None:

    # Main program entry.

    if is_virtual_environment():
        print("\nMATRIX STATUS: Welcome to the construct\n")
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")

    show_environment_info()


if __name__ == "__main__":
    main()
