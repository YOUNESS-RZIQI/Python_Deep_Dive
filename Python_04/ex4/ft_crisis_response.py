try:

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    try:

        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt") as fd_o:
            print("SUCCESS: Archive recovered - ``", end="")
            print(fd_o.read(), "''", sep="")

        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, system stable\n")

    try:

        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt") as fd_o:
            print("SUCCESS: Archive recovered - ``", end="")
            print(fd_o.read(), "''", sep="")

        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, system stable\n")

    try:

        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt") as fd_o:
            print("SUCCESS: Archive recovered - ``", end="")
            print(fd_o.read(), "''", sep="")

        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, system stable\n")

    print("All crisis scenarios handled successfully. Archives secure.")
except Exception as e:
    print("Error :", e)
