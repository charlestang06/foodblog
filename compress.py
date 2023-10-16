import os
from PIL import Image

def compress_images_with_numbers(folder_path):
    # Get the absolute path of the "_recipes" subfolder
    subfolder_path = os.path.abspath(os.path.join(folder_path, "_recipes"))

    # Check if the subfolder exists
    if not os.path.exists(subfolder_path) or not os.path.isdir(subfolder_path):
        print(f"Subfolder '{subfolder_path}' does not exist.")
        return

    # Iterate over the files in the subfolder
    for filename in os.listdir(subfolder_path):
        file_path = os.path.join(subfolder_path, filename)

        # Check if the file is a JPEG image with a number in its name
        if filename.lower().endswith(".jpg") and "chickenadobo" in filename: # and any(char.isdigit() for char in filename) and "stamppot" in filename:
            try:
                # Open the image using PIL
                image = Image.open(file_path)

                # Compress the image (adjust the quality as desired)
                compressed_image = image.copy()
                compressed_image.save(file_path, "JPEG", quality=20)

                print(f"Compressed image: {file_path}")

            except Exception as e:
                print(f"Failed to compress image: {file_path}")
                print(str(e))

# Provide the parent folder path where "_recipes" subfolder exists
folder_path = ""

compress_images_with_numbers(folder_path)
