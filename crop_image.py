import os
from PIL import Image

# Set the path of the folder containing the original images and the destination folder path
input_folder = "PATH TO IMAGES"
output_folder = "PATH TO OUTPUT"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through each file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith((".tif", ".jpg", ".jpeg")):  # Check if the file is an image
        # Open the image
        image = Image.open(os.path.join(input_folder, filename))

        # Check if the image size is 6000x6000
        if image.size == (6000, 6000):
            # Crop the image into 16 images of size 1500x1500
            for i in range(4):
                for j in range(4):
                    left = j * 1500
                    top = i * 1500
                    right = left + 1500
                    bottom = top + 1500

                    cropped_image = image.crop((left, top, right, bottom))

                    # Save the cropped images in the output folder
                    base_filename, file_extension = os.path.splitext(filename)
                    cropped_image.save(os.path.join(output_folder, f"{base_filename}_{i+4*j}{file_extension}"))
        else:
            print(f"The image {filename} does not have dimensions 6000x6000. Ignored.")
