import os
import json
import zipfile

# Define the file and directory paths
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, 'skynet.json')
build_dir = os.path.abspath(os.path.join(current_dir, '../builds'))

# Load version from skynet.json
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    version = data.get('ver')
    if not version:
        raise ValueError("Version not found in skynet.json")

# Name of the output zip file
zip_filename = f"SKYNET-{version}.zip"
zip_filepath = os.path.join(build_dir, zip_filename)

# Ensure the ../builds directory exists
if not os.path.exists(build_dir):
    os.makedirs(build_dir)

# Create a zip file
with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            # Exclude the builds directory itself from being zipped
            if file != zip_filename:
                file_path = os.path.join(root, file)
                # Add the file to the zip, ensuring the relative path is used
                arcname = os.path.relpath(file_path, current_dir)
                zipf.write(file_path, arcname)

print(f"Directory zipped successfully into {zip_filepath}")
