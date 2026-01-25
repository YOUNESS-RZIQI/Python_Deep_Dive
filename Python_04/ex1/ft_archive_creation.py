try:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    fd_o = open("new_discovery.txt", "w")

    print("Initializing new storage unit: new_discovery.txt")
    data = "[ENTRY 001] New quantum algorithm discovered\n\
[ENTRY 002] Efficiency increased by 347%\n\
[ENTRY 003] Archived by Data Archivist trainee"
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")

    fd_o.write(data)
    print(data)
    print("\nData inscription complete. Storage unit sealed.")

    fd_o.close()
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
except Exception as e:
    print(e)
