try:
    fd_o = open("ancient_fragment.txt")

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {fd_o.name}\n"
          "Connection established...\n")

    data = fd_o.read()
    print(data)
    fd_o.close()

    print("\nData recovery complete. Storage unit disconnected.")

except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")

except Exception as e:
    print(e)
