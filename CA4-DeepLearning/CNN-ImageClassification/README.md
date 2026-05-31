# Task 2: Flower Image Classification using CNNs

## 📖 Overview

The primary objective of this project is to explore the trade-offs between designing a custom neural network architecture from scratch versus leveraging transfer learning. The notebook utilizes a multi-class flower dataset from Kaggle to train a custom VGG-style CNN and fine-tune a pre-trained ResNet model, directly comparing their efficiency and accuracy.

## ✨ Key Features & Objectives

* **Automated Data Ingestion:** Uses `kagglehub` to directly download and manage the `flowers-multiclass-datasets`.
* **Custom VGG-Style CNN:** Designing and training a Convolutional Neural Network from scratch, mirroring the architectural principles of VGG networks.
* **Transfer Learning (ResNet):** Adapting and fine-tuning a pre-trained ResNet model for the specific task of flower classification to evaluate improvements in training time and predictive accuracy.
* **Comprehensive Evaluation:** Implementing performance metrics and visualizations, including displaying the Confusion Matrix and ROC Curves for the classification results.
* **Theoretical Analysis (Parameter Calculation):** Manually calculating and comparing the number of learnable parameters in a standard Convolutional Layer ($2\times2\times3$ filters) versus a fully connected Dense Layer to demonstrate the parameter efficiency of CNNs.

## 📊 Results & Outputs

Upon executing the notebook, the following evaluations are produced:

* **Model Comparison:** A direct comparison of accuracy and loss between the custom VGG-style network and the fine-tuned ResNet model.
* **Visual Metrics:** Generation of confusion matrices (`print_confusion_matrix`) and ROC curves (`display_ROC_curve`) to assess the model's performance across different flower classes.
* **Bonus Question Answer:** The notebook mathematically proves that a specific convolutional layer requires exactly 39 parameters, whereas replicating its behavior with a fully connected layer would require drastically more parameters ($>2$ million), highlighting why CNNs are computationally superior for image data.

## 🛠️ Tech Stack & Requirements

To run the notebook successfully, ensure the following Python libraries are installed:

* **Deep Learning Framework:** PyTorch or TensorFlow/Keras (depending on the environment execution)
* **Data & Tooling:** `kagglehub`
* **Visualization:** `matplotlib` / `seaborn` (for ROC and Confusion Matrix plotting)
* **Metrics:** `scikit-learn`

