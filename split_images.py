import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(images_path, ground_truth_path, output_path):
    # List files in directories
    images = sorted(os.listdir(images_path))
    ground_truths = sorted(os.listdir(ground_truth_path))
    
    # Split files into training, validation, and test sets
    train_images, temp_images, train_gt, temp_gt = train_test_split(images, ground_truths, test_size=0.2, random_state=42)
    val_images, test_images, val_gt, test_gt = train_test_split(temp_images, temp_gt, test_size=0.5, random_state=42)
    
    # Create output directories if they don't exist
    os.makedirs(os.path.join(output_path, 'train', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_path, 'train', 'ground_truth'), exist_ok=True)
    os.makedirs(os.path.join(output_path, 'val', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_path, 'val', 'ground_truth'), exist_ok=True)
    os.makedirs(os.path.join(output_path, 'test', 'images'), exist_ok=True)
    os.makedirs(os.path.join(output_path, 'test', 'ground_truth'), exist_ok=True)

    # Copy files to the corresponding directories
    for img, gt in zip(train_images, train_gt):
        shutil.copy(os.path.join(images_path, img), os.path.join(output_path, 'train', 'images', img))
        shutil.copy(os.path.join(ground_truth_path, gt), os.path.join(output_path, 'train', 'ground_truth', gt))

    for img, gt in zip(val_images, val_gt):
        shutil.copy(os.path.join(images_path, img), os.path.join(output_path, 'val', 'images', img))
        shutil.copy(os.path.join(ground_truth_path, gt), os.path.join(output_path, 'val', 'ground_truth', gt))
        
    for img, gt in zip(test_images, test_gt):
        shutil.copy(os.path.join(images_path, img), os.path.join(output_path, 'test', 'images', img))
        shutil.copy(os.path.join(ground_truth_path, gt), os.path.join(output_path, 'test', 'ground_truth', gt))


# Paths to directories (adjust these paths according to your directory)
images_path = 'PATH TO IMAGES'
ground_truth_path = 'PATH TO GROUND TRUTH'
output_path = 'PATH TO OUTPUT'

# Call the function to split the dataset
split_dataset(images_path, ground_truth_path, output_path)
