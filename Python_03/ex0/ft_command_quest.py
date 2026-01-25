try:
    import sys

    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print("Program name:", sys.argv[0])
    else:
        print("Program name:", sys.argv[0])
        print("Arguments received:", len(sys.argv) - 1)
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")

    print("Total arguments:", len(sys.argv))
except Exception as e:
    print("Error : ", e)
