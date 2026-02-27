import sys
import importlib


def check_dependency(name: str) -> bool:
    # Check if a module is installed and print its version
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        message = ""
        if name == "pandas":
            message = "Data manipulation ready"
        elif name == "numpy":
            message = "Numerical computations ready"
        else:
            message = "Visualization ready"

        print(f"[OK] {name} ({version}) - {message}")
        return True
    except ImportError:
        print(f"[MISSING] {name} - Not installed")
        return False


def analyze_data() -> None:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    # Generate sample data
    data = np.random.randint(1, 100, size=20)
    df = pd.DataFrame({"values": data})

    print(f"Processing {len(df)} data points...")

    # Simple matplotlib plot (no styling)
    plt.plot(df["values"])
    plt.title("Matrix Data")
    plt.xlabel("Index")
    plt.ylabel("Value")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Visualization saved to: matrix_analysis.png")
    print("Analysis complete!")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:\n")

    required = ["pandas", "numpy", "matplotlib"]

    all_ok = True

    for package in required:
        if not check_dependency(package):
            all_ok = False

    if not all_ok:
        print("\nSome dependencies are missing.")
        print("Install using:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        return

    analyze_data()


if __name__ == "__main__":
    main()
