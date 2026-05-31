# Task 3: Bitcoin Price Forecasting using RNN & LSTM

This repository contains the Jupyter Notebook implementation (`Task3.ipynb`) for the final task of the Data Science Deep Learning assignment. The project focuses on time-series forecasting, specifically utilizing Recurrent Neural Networks (RNN) and Long Short-Term Memory (LSTM) networks to predict the future price of Bitcoin based on historical financial data.

## 📖 Overview

The primary objective of this project is to explore sequence modeling for financial time-series data. By preprocessing historical Bitcoin prices and structuring them into sequential windows, the notebook trains standard RNN and advanced LSTM models to predict future price points. A major focus of the task is analyzing the limitations of standard RNNs—specifically the vanishing gradient problem—and demonstrating how LSTMs mitigate these issues over longer sequences.

## ✨ Key Features & Objectives

* **Time-Series Preprocessing:** Handling raw financial data using `pandas`, and applying robust scaling techniques (`MinMaxScaler`, `StandardScaler`) via `scikit-learn` to normalize the data for neural network ingestion.
* **Sliding Window Generation:** Structuring the continuous time-series data into discrete "lookback" windows (sequences) to train the recurrent models.
* **Model Implementations (Keras):** Designing and compiling both `SimpleRNN` and `LSTM` (including `Bidirectional` implementations) using the TensorFlow/Keras framework.
* **Training Optimization:** Utilizing the `Adam` optimizer, `MeanSquaredError` loss functions, and implementing `EarlyStopping` callbacks to prevent model overfitting.
* **Theoretical Analysis:** A deep dive into the mathematics of the **Vanishing Gradient Problem** in RNNs during Backpropagation Through Time (BPTT), specifically addressing how the lookback window size severely impacts gradient stability.

## 📊 Results & Outputs

Upon executing the notebook, the following evaluations and insights are produced:

* **Model Comparison:** A direct evaluation of the predictive accuracy (using Mean Squared Error and Mean Absolute Error) between the standard RNN and the LSTM models.
* **Visual Forecasting:** Matplotlib and Seaborn plots visualizing the model's predicted Bitcoin prices overlaid against the actual historical test data.
* **Mathematical Proof (Vanishing Gradients):** The notebook formally explains that because the gradient derivative $\frac{\partial h_t}{\partial h_{t-1}}$ relies on the recurrent weight matrix and the derivative of the $tanh$ function (which is $<1$), repeated multiplications over time steps cause the gradient to decay toward zero. The analysis explicitly proves that **larger lookback windows** introduce more multiplications, drastically exacerbating the vanishing gradient effect in vanilla RNNs.

## 🛠️ Tech Stack & Requirements

To run the notebook successfully, ensure the following Python libraries are installed:

* **Deep Learning Framework:** `tensorflow` (specifically `tensorflow.keras`)
* **Data Processing:** `pandas`, `numpy`, `scikit-learn`
* **Visualization:** `matplotlib`, `seaborn`
* *(Note: `torch` and its utilities are also imported as alternative backend resources)*.
