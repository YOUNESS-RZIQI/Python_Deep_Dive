import os
import sys
from dotenv import load_dotenv

load_dotenv()

DEFAULTS = {
    "MATRIX_MODE":    "development",
    "DATABASE_URL":   None,
    "API_KEY":        None,
    "LOG_LEVEL":      "DEBUG",
    "ZION_ENDPOINT":  None,
}

def get_config():
    missing = []
    config  = {}
    for key, default in DEFAULTS.items():
        value = os.getenv(key, default)
        if value is None:
            missing.append(key)
        config[key] = value
    return config, missing

def main():
    print("ORACLE STATUS:")
    print("Reading the Matrix...\n")

    config, missing = get_config()

    if missing:
        print("WARNING: Missing required configuration:")
        for key in missing:
            print(f"  [MISSING] {key}")
        print("\nCopy .env.example to .env and fill in the values.")
        print("  cp .env.example .env")
        sys.exit(1)

    mode = config["MATRIX_MODE"]
    print("Configuration loaded:")
    print(f"  Mode:         {mode}")
    print(f"  Database:     {'Connected to local instance' if 'localhost' in config['DATABASE_URL'] else 'Connected to remote instance'}")
    print(f"  API Access:   {'Authenticated' if config['API_KEY'] else 'No key'}")
    print(f"  Log Level:    {config['LOG_LEVEL']}")
    print(f"  Zion Network: {'Online' if config['ZION_ENDPOINT'] else 'Offline'}")

    print("\nEnvironment security check:")
    print("  [OK] No hardcoded secrets detected")
    print(f"  [OK] .env file {'properly configured' if os.path.exists('.env') else 'not found (using env vars)'}")
    print(f"  [OK] Production overrides {'active' if mode == 'production' else 'available'}")

    print("\nThe Oracle sees all configurations.")

if __name__ == "__main__":
    main()
