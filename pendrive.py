import os
import shutil
import tempfile
import string
import random

# Utility function to generate random data
def generate_random_data(size_in_bytes):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size_in_bytes)).encode()

# Function to get available drives
def get_available_drives():
    drives = []
    for drive in string.ascii_uppercase:
        if os.path.exists(f"{drive}:\\"):
            drives.append(f"{drive}:\\")
    return drives

# Function to check if the selected drive is a valid pendrive
def is_valid_pendrive(drive):
    if drive.upper() in ['C:\\', 'D:\\']:
        return False
    if os.path.ismount(drive):
        return True
    return False

# Function to get drive size (in bytes)
def get_drive_size(drive):
    total, used, free = shutil.disk_usage(drive)
    return total, used, free

# Function to fill the drive with temporary files and calculate actual storage size
def fill_drive(drive):
    total_size_before, used_before, free_before = get_drive_size(drive)
    
    print(f"Filling {drive} with data...")
    temp_dir = os.path.join(drive, 'temp_fill')
    os.makedirs(temp_dir, exist_ok=True)
    
    total_written_data = 0  # Track the total data written
    file_counter = 0  # To count the number of files written
    
    try:
        while True:
            # Generate a temporary file name
            temp_file_path = os.path.join(temp_dir, f'tempfile_{file_counter}.dat')
            file_size = 1024 * 1024 * 100  # Write 100 MB at a time

            # Create and write data to the temporary file
            with open(temp_file_path, 'wb') as temp_file:
                temp_file.write(generate_random_data(file_size))
            
            total_written_data += file_size
            file_counter += 1

    except OSError:
        # OSError happens when the disk is full
        print(f"{drive} is now full.")

    total_size_after, used_after, free_after = get_drive_size(drive)
    return total_written_data, temp_dir

# Function to clean up the temporary files
def clean_up(temp_dir):
    print(f"Cleaning up files in {temp_dir}...")
    shutil.rmtree(temp_dir)

# Main function to execute the storage size check
def main():
    drives = get_available_drives()
    
    print("Available drives:")
    for i, drive in enumerate(drives):
        print(f"{i+1}. {drive}")

    # Get the user's choice of drive
    while True:
        try:
            choice = int(input("Select the drive number to check (not C or D): "))
            if choice < 1 or choice > len(drives):
                print("Invalid choice. Please select a valid drive.")
                continue
            
            selected_drive = drives[choice - 1]
            
            if is_valid_pendrive(selected_drive):
                break
            else:
                print(f"{selected_drive} is not a valid pendrive or is a local disk.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Fill the selected drive and measure its storage
    actual_storage_written, temp_dir = fill_drive(selected_drive)

    print(f"Actual storage filled with data: {actual_storage_written / (1024 * 1024 * 1024):.2f} GB")

    # Clean up the temp files
    clean_up(temp_dir)
    print(f"All temporary files removed from {selected_drive}.")

if __name__ == "__main__":
    main()
