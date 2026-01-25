try:

    import sys

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    report_status = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {archivist_id}: {report_status}")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels"
                     " verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete")
    sys.stdout.write("\nThree-channel communication test successful.")

except Exception:
    sys.stderr.write("Three-channel communication test Rejected ! !\n")
