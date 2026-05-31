# Deep Learning Applications: MLP, CNN, and RNN

## 📖 Overview

This repository contains the implementation for Data Science Assignment 4. The project is divided into three distinct deep learning tasks, each focusing on designing, implementing, and evaluating different neural network architectures (MLP, CNN, and RNN) to solve real-world challenges across various domains.

## 🎯 Main Objectives & Tasks

1. **Football Match Prediction (MLP):** Design and train a Multi-Layer Perceptron (MLP) using historical football match data to predict the outcomes of the qualifiers and the Qatar 2022 FIFA World Cup.
2. **Flower Image Classification (CNN):** Build a Convolutional Neural Network (CNN) to classify images of flowers. This involves creating a VGG-style CNN from scratch and fine-tuning a pre-trained ResNet model to compare the benefits of custom architecture versus transfer learning.
3. **Bitcoin Price Prediction (RNN & LSTM):** Preprocess time-series financial data to forecast Bitcoin prices. Experiment with standard Recurrent Neural Networks (RNN) and Long Short-Term Memory (LSTM) models to evaluate their predictive accuracy and ability to capture long-term dependencies.

## 🧠 Core Concepts Explored

* **Multi-Layer Perceptrons (MLP):** Understanding dense layers, activation functions, and their equivalence to models like Logistic Regression under specific conditions.
* **Convolutional Neural Networks (CNN):** Working with convolutional layers, pooling, learnable parameter calculations, and transfer learning (ResNet).
* **Recurrent Neural Networks (RNN & LSTM):** Handling sequential time-series data, sliding windows (lookback size), and utilizing LSTMs to mitigate the vanishing gradient problem inherent in vanilla RNNs.
* **Deep Learning Frameworks:** Implementing and training models using PyTorch (Task 1) and TensorFlow/Keras (Task 3).

## 🛠️ Tech Stack

* **Language:** Python 3
* **Deep Learning Frameworks:** `PyTorch`, `TensorFlow` / `Keras`
* **Data Processing:** `pandas`, `numpy`, `scikit-learn` (MinMaxScaler, StandardScaler)
* **Visualization:** `matplotlib`, `seaborn`
