import os

# Path to your attendance.csv file
file_path = 'attendance.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Open the file in write mode ('w')
    with open(file_path, 'w') as file:
        # Truncate the file to clear its content
        file.truncate(0)
        print(f"File '{file_path}' cleared successfully.")
else:
    print(f"File '{file_path}' does not exist.")
