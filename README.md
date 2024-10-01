# Cancer Prediction Using Skin Images

This project focuses on predicting the type of cancer by analyzing images of affected skin areas. By leveraging machine learning models, the project classifies the type of skin cancer based on dermatoscopic images. This solution aims to assist in early cancer detection, which can significantly improve treatment outcomes.

## Project Overview

The primary objective of this project is to develop a machine learning model that takes an image of an affected skin area and categorizes it into different types of cancer. We have implemented a **Random Forest Classifier** for the prediction and evaluated the performance of other models such as **Logistic Regression**, **Decision Tree Classifier**, and **K-Neighbors Classifier**.

### Dataset

The project uses the **HAM10000 Dataset**, a large collection of multi-source dermatoscopic images. This dataset includes 10,015 dermatoscopic images for academic machine learning purposes and covers all important diagnostic categories related to pigmented lesions.

- **Source**: [HAM10000 on Kaggle](https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000)
- **Images**: 10,015 images of skin lesions
- **Preprocessing**: The images are resized to 28x28 pixels. Each image is converted into a numerical format where each pixel's value is represented in a CSV file with 784 columns (28x28 pixels). Each row in the dataset represents one image.

### Models Used

We implemented multiple machine learning models and compared their performance in terms of accuracy, precision, recall, and other metrics. The models we used include:

- **Random Forest Classifier**: A powerful ensemble learning method that works by constructing multiple decision trees during training and outputs the class that is the mode of the classes.
- **Logistic Regression**: A popular linear model for binary classification that applies the logistic function to model a binary dependent variable.
- **Decision Tree Classifier**: A non-parametric supervised learning method that is simple to interpret and implement.
- **K-Neighbors Classifier**: A non-parametric algorithm that classifies instances based on their proximity to training data points.

### Performance Evaluation

After training and testing the models, we evaluated the following key performance metrics:

- **Accuracy**: Measures the percentage of correct predictions.
- **Precision**: Measures the proportion of positive identifications that were actually correct.
- **Recall**: Measures the proportion of actual positives that were identified correctly.

Based on these metrics, the **Random Forest Classifier** showed the best overall performance, but other models also provided valuable insights and comparisons.

### Data Visualization

To gain insights into the dataset and model predictions, data visualization techniques were applied. Python's `matplotlib` and `seaborn` libraries were used for visualizing the results and exploring the data trends.

### GUI for Cancer Prediction

A simple **Graphical User Interface (GUI)** has been designed using Python's `Tkinter` library. This GUI allows users to upload an image of a skin lesion, which is then processed by the machine learning model to predict the type of cancer.

- **File**: `Gui.py`
- The GUI is easy to use and provides an intuitive interface for making predictions.

## Dependencies

The project uses several Python libraries for data processing, model building, and visualization. Ensure the following dependencies are installed:

  ```bash
  pip install pandas numpy matplotlib scikit-learn tkinter
  ```

## Future Work
The current project focuses on Random Forest and a few other machine learning models. In the future, we plan to extend this project by adding:
- Deep Learning: We will experiment with Convolutional Neural Networks (CNNs) to improve prediction accuracy.
- Data Augmentation: To increase the size of the training dataset for better generalization.
