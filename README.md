

<div align="center">
<h1 align="center">
<img src="NN.svg" width="200" />
<br>
Sematic-Segmentation-on-Podsdam-ISPRS
</h1>
<h3 align="center">📍 Unleash the power of accurate semantic segmentation with Podsdam-ISPRS on GitHub!</h3>
<h3 align="center">⚙️ Developed with the software and tools below:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" alt="Jupyter" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white" alt="Python" />
</p>
</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [🚀 Introduction](#-introduction)
- [📍 Objective](#-objective)   
- [💫 Features](#-features)
- [📊 Dataset](#-dataset)
- [🖌 Usage](#-usage)
- [📈 Results and Evaluation](#-results-and-evaluation)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🚀 Introduction:

Semantic segmentation is a fundamental task in computer vision that aims to assign a specific class label to each pixel in an image. Unlike object detection or classification, which focus on identifying objects or predicting labels for the entire image, semantic segmentation provides a detailed understanding of the image at the pixel level. By segmenting an image into distinct regions corresponding to different object classes or semantic categories, semantic segmentation enables advanced visual understanding and scene analysis.

In semantic segmentation, the goal is to create a pixel-wise prediction map that accurately delineates the boundaries and regions of different objects or semantic concepts within an image. This fine-grained level of analysis allows for precise localization and identification of objects, making it a crucial task in applications such as autonomous driving, image editing, virtual reality, and medical image analysis.

Achieving accurate and robust semantic segmentation requires the development of sophisticated deep learning models capable of capturing the intricate details and spatial dependencies present in images. By leveraging powerful convolutional neural networks (CNNs) and advanced architectural designs, researchers have made significant progress in semantic segmentation, pushing the boundaries of what computers can perceive and understand in visual data.

However, along with model development, the quality and suitability of the dataset used for training are of utmost importance. Cleaning and preparing the dataset is a critical step to ensure that the model learns from reliable and representative examples. By addressing challenges like noisy annotations, class imbalance, and inconsistent labeling, we can enhance the dataset's quality, leading to improved model performance and generalization.

In this project, our objective is to construct a neural network model for semantic segmentation and train it on a meticulously curated dataset. By focusing on both the model architecture and the dataset preprocessing, we aim to achieve state-of-the-art performance in semantic segmentation while contributing to the broader advancement of computer vision research and applications.

## 📍 Objective:

The objective of this project is to develop a neural network model for semantic segmentation and train it on a carefully prepared dataset. In addition to implementing the model, a significant part of the project involves the data preprocessing stage, where we focus on cleaning and preparing the dataset to optimize the model's performance. By meticulously examining and addressing potential issues such as noise, class imbalance, and inconsistent annotations, we aim to create a high-quality dataset that can effectively train the neural network model for accurate and robust semantic segmentation. Through this project, we strive to improve the state-of-the-art in semantic segmentation and contribute to the advancement of computer vision research and applications.
 


---

## 💫 Features

Feature | Description |
|---|---|
| **🏗 Structure and Organization** | The codebase is well-organized, with separate folders for data, models, and metrics, and well-named files that reflect their functionality. The main files are easy to find and contain clear entry points. |
| **📝 Code Documentation** | The code benefits from descriptive variable names and code comments, allowing for easier understanding by others. |
| **🧩 Dependency Management** | Dependencies are listed in a `requirements.txt` file, and the installation script is properly documented. |
| **♻️ Modularity and Reusability** | The code is highly modular with most functionality implemented through functions that can be reused. Data handling operations have their separate file, allowing this to be reused, even replacing the images dataset. New models can be added easily with minimal changes to existing codebase. |
| **✔️ Testing and Quality Assurance** | The code lacks proper testing. However, the classifier details are provided and metrics help assess the quality of the segmentation output by means of Intersection over Union (IoU), Precision, and Recall values for every class straight away. |
| **⚡️ Performance and Optimization** | The segmentation model is implemented in `Pytorch` and includes several efficient approaches including `batch normalization`, `max poolings`, and `convolving`. However, model fitting can take a long time depending on the complexity of the images and models provided. |
| **🔌 External Integrations** | The codebase integrates with powerful libraries such as `Pytorch` and `scikit-learn` for modeling.|

---
##  📊 Dataset

This dataset consists of high-resolution aerial data containing a variety of urban objects. Six categories/classes have been defined:

- Impervious surfaces (RGB: 255, 255, 255)
- Building (RGB: 0, 0, 255)
- Low vegetation (RGB: 0, 255, 255)
- Tree (RGB: 0, 255, 0)
- Car (RGB: 255, 255, 0)
- Clutter/background (RGB: 255, 0, 0)

---

## 🖌 Usage

This dataset can be used by researchers and developers to:

- Develop and test algorithms for urban object detection and classification.
- Develop and test algorithms for building reconstruction.
- Evaluate the performance of algorithms on high-resolution aerial data.
- Understand the context information of urban objects for improved extraction results.
---

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

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## 📂 Project Structure


```bash
repo
├── crop_image.py
├── split_images.py
└── urban-object-extraction
    └── main.ipynb

2 directories, 3 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 🧩 Modules

<details closed><summary>Root</summary>

| File            | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                   | Module          |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| crop_image.py   | The code loops through a folder containing image files and crops any image that's 6000x6000 into sixteen smaller images with the size of 1500x1500. The cropped images are then saved into a separate destination folder. The code includes functions for checking the size of the image and creates a new folder automatically if it doesn't exist.                                                                                      | crop_image.py   |
| split_images.py | The code splits a dataset of images and ground truth data into training, validation, and test sets using the `train_test_split` function from the `scikit-learn` library. It then creates directories for each set of data and copies the corresponding images and ground truth files into their respective directories using the `os` and `shutil` libraries. The purpose of this code is to prepare data for machine learning projects. | split_images.py |

</details>

<details closed><summary>Urban-object-extraction</summary>

| File       | Summary                                                                                                                       | Module                             |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------|
| main.ipynb | The complete Jupyter code of the implementation | urban-object-extraction/main.ipynb |
|            |                                                                  |                                    |

</details>

---

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> -  python
> -  pytorch
> -  numpy
> -  matplotlib
> -  scikit-learn

### 🖥 Installation

1. Clone the Sematic-Segmentation-on-Podsdam-ISPRS repository:
```sh
git clone https://github.com/giumanuz/Sematic-Segmentation-on-Podsdam-ISPRS
```

2. Change to the project directory:
```sh
cd Sematic-Segmentation-on-Podsdam-ISPRS
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```
4. [Download the dataset](https://www.isprs.org/education/benchmarks/UrbanSemLab/default.aspx). The dataset is organized into different directories representing various urban object classes. Please refer to the documentation for the structure and description of the dataset.

5. The original images in the dataset are cropped into smaller images. By default, each image is cropped into 16 smaller images. However, you can use the provided code in `crop_image.py` to crop the images into an arbitrary number of smaller images.

6. The `split_images.py` script is used to create the training, testing, and validation datasets. You can set arbitrary proportions for splitting the dataset. By default the dataset is split into 80% training, 10% testing, and 10% validation.

7. Use the data as per your research or project requirements. Please make sure to cite this dataset if you use it in your research or project.

---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `MIT` License. 

---
