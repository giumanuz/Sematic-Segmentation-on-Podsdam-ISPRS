# Urban Object Extraction Dataset

## Introduction

Welcome to the Urban Object Extraction Dataset repository! The automated extraction of urban objects from aerial data has been a crucial research topic in photogrammetry for the past two decades. However, most research papers tend to focus on the extraction of a single object class such as buildings, roads, or trees. Our aim is to provide a state-of-the-art dataset that allows researchers to test and develop their methods and algorithms on a diverse set of urban object classes, sometimes simultaneously.

## Objective

This project is aimed at facilitating the development of algorithms for urban object classification and building reconstruction. Participants can choose to focus on detecting single object classes or multiple object classes at the same time. Extracting multiple object classes simultaneously can be beneficial as it allows algorithms to make use of context information, that is, information contained in the mutual arrangement of objects in complex urban scenes. 

## Dataset

This dataset consists of high-resolution aerial data containing a variety of urban objects. Six categories/classes have been defined:

- Impervious surfaces (RGB: 255, 255, 255)
- Building (RGB: 0, 0, 255)
- Low vegetation (RGB: 0, 255, 255)
- Tree (RGB: 0, 255, 0)
- Car (RGB: 255, 255, 0)
- Clutter/background (RGB: 255, 0, 0)

## Usage

This dataset can be used by researchers and developers to:

- Develop and test algorithms for urban object detection and classification.
- Develop and test algorithms for building reconstruction.
- Evaluate the performance of algorithms on high-resolution aerial data.
- Understand the context information of urban objects for improved extraction results.

## Getting Started

1. Clone this repository to your local machine.
    ```sh
    git clone https://github.com/giumanuz/Sematic-Segmentation-on-Podsdam-ISPRS
    ```

2. Navigate to the directory.
    ```sh
    cd urban-object-extraction-dataset
    ```

3. [Download the dataset](https://www.isprs.org/education/benchmarks/UrbanSemLab/default.aspx). The dataset is organized into different directories representing various urban object classes. Please refer to the documentation for the structure and description of the dataset.

4. The original images in the dataset are cropped into smaller images. By default, each image is cropped into 16 smaller images. However, you can use the provided code in `crop_image.py` to crop the images into an arbitrary number of smaller images.

5. The `split_images.py` script is used to create the training, testing, and validation datasets. You can set arbitrary proportions for splitting the dataset. By default the dataset is split into 80% training, 10% testing, and 10% validation.

6. Use the data as per your research or project requirements. Please make sure to cite this dataset if you use it in your research or project.

## Results and Evaluation

### Accuracy

Using the provided dataset and running the model for 100 epochs, an accuracy of approximately 79% is achieved. The performance can vary based on different parameters and configurations, but this gives a baseline of what to expect with the current settings.

### Confusion Matrix

A confusion matrix is essential for understanding how the model performs in classifying different urban objects. Below is the confusion matrix obtained from running the model with the given dataset:

<div align="center">
    <img src="confusion_matrix.png" alt="Description of image" width="500"/>
</div>

### Sample Predicted and Output Labels

Here are sample images showing the predicted labels and the actual output labels obtained using the model. These examples provide a visual representation of how the model performs in classifying urban objects:

**Example with resize from 1500x1500 to 96x96:**
<div align="center">
    <img src="example1.png" alt="Description of image" width="800"/>
</div>

**Second example:**
<div align="center">
    <img src="example2.png" alt="Description of image" width="800"/>
</div>






## Contributing

We welcome contributions to this dataset. If you have suggestions, corrections, or additions to the dataset, please submit a pull request or create an issue.


## License

This dataset is released under the MIT License. See the `LICENSE` file for more information.

## Contact

- Giulio Manuzzi
- giuliomanuzzi@gmail.com

Feel free to reach out if you have any questions or need further information. Happy coding!
