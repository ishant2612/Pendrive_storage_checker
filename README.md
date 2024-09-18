# Drive Storage Filler

This script fills a selected drive (excluding local disks) with temporary files to test its storage capacity and then cleans up the files. It helps determine the actual usable storage space of a drive by writing a large amount of random data to it.

## Features

- **Generate Random Data**: Creates random data to fill the drive.
- **Drive Detection**: Lists available drives excluding common local disks (C: and D:).
- **Drive Validation**: Ensures that the selected drive is a valid external drive.
- **Drive Size Calculation**: Measures the storage space before and after filling the drive.
- **Temporary File Cleanup**: Removes all generated temporary files after the test.

## Requirements

- Python 3.x
- `shutil`, `tempfile`, `os`, `string`, and `random` modules (standard library)

## Usage

1. **Run the Script**:
   - Execute the script using Python 3:
     ```bash
     python pendrive.py
     ```

2. **Select a Drive**:
   - The script will list available drives. Choose the drive you want to test (must be an external drive, not C: or D:).

3. **Filling the Drive**:
   - The script will begin filling the selected drive with temporary files. It will display the amount of storage used.

4. **Cleanup**:
   - Once the drive is full, the script will clean up all temporary files created during the test.

## How It Works

1. **Drive Detection**: The script detects available drives and filters out common local disks.
2. **Drive Validation**: Checks if the selected drive is an external drive.
3. **Filling the Drive**: Writes 100 MB chunks of random data to the drive until it's full.
4. **Cleanup**: Removes all generated files from the drive.

## Notes

- Be cautious when running this script as it will fill the selected drive completely.
- Ensure that no important data is stored on the drive being tested.
- This script may take some time to run depending on the size of the drive and the speed of the writing process.


## Author

This script was created by Ishant Verma.

## Contact

For any questions or feedback, please contact Ishant Verma at [vishant448@gmail.com](mailto:vishant448@gmail.com).
