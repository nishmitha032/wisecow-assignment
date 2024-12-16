import os
import time

# Directory to back up
BACKUP_DIR = "C:\\Users\\maila\\Downloads\\wisecow-assignment"  # Replace with your path
BACKUP_NAME = f"backup_{time.strftime('%Y%m%d_%H%M%S')}.zip"

# Create a zip backup
def create_backup():
    print("Creating backup...")
    os.system(f"tar -czvf {BACKUP_NAME} {BACKUP_DIR}")
    print(f"Backup created: {BACKUP_NAME}")

# Main function
if __name__ == "__main__":
    create_backup()
