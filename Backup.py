import os
import sys
import shutil
from datetime import datetime
 
 
def backup_files(source_dir, destination_dir):
 
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
 
    if not os.path.isdir(destination_dir):
        print(f"Error: Destination directory '{destination_dir}' does not exist.")
        return
 
    try:
 
        for filename in os.listdir(source_dir):
 
            source_file = os.path.join(source_dir, filename)
 
            if not os.path.isfile(source_file):
                continue
 
            dest_file = os.path.join(destination_dir, filename)
 
            if os.path.exists(dest_file):
                base, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_filename = f"{base}_{timestamp}{ext}"
                dest_file = os.path.join(destination_dir, new_filename)
                print(f"Duplicate found. Renaming to: {new_filename}")
 
            shutil.copy2(source_file, dest_file)
            print(f"Backed up: {filename}")
 
        print("\nBackup completed successfully!")
 
    except Exception as e:
        print(f"An error occurred during backup: {e}")
 
 
if __name__ == "__main__":
   
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)
 
    source = sys.argv[1]
    destination = sys.argv[2]
 
    backup_files(source, destination)
