"""Backup generated content and configuration."""


import json
from datetime import datetime


def main():
    backup_data = {
        "timestamp": datetime.now().isoformat(),
        "version": "0.1.0",
    }
    filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(backup_data, f, indent=2)
    print(f"Backup saved to {filename}")


if __name__ == "__main__":
    main()
