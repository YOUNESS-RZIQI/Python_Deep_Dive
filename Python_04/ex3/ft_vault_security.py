try:

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    with open("classified_data.txt") as fd_o:
        print("SECURE EXTRACTION:")
        data = fd_o.read()
        print(data, "\n", sep="")

    with open("security_protocols.txt") as fd_o:
        print("SECURE PRESERVATION:")
        data = fd_o.read()
        print(data)
        print("Vault automatically sealed upon completion\n")

    print("All vault operations completed with maximum security.")

except Exception as e:
    print(e)
