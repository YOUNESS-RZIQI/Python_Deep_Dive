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
    # import numpy as numpy
    # import pandas as pandas
    # import matplotlib.pyplot as matplotlib.pyplot

    print("\nAnalyzing Matrix data...")

    # Generate sample data
    data = numpy.random.randint(1, 100, size=1000)
    df = pandas.DataFrame({"values": data})

    print(f"Processing {len(df)} data points...")

    # Simple matplotlib plot (no styling)
    matplotlib.pyplot.plot(df["values"])
    matplotlib.pyplot.title("Matrix Data")
    matplotlib.pyplot.xlabel("Index")
    matplotlib.pyplot.ylabel("Value")

    matplotlib.pyplot.savefig("matrix_analysis.png")
    matplotlib.pyplot.close()

    print("Generating visualization...")
    print("\nAnalysis complete!")
    print("Results saved to: matrix\\_analysis.png}")


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
