# FIFA World Cup 2022 Prediction using Multi-Layer Perceptrons (MLP)

## 📖 Overview

The primary objective of this project is to leverage historical football match data to forecast the results of the **Qatar 2022 FIFA World Cup**. By feeding data from qualifiers and past tournaments into a custom-built neural network, the model learns team performance patterns and simulates the tournament's knockout stages to predict the ultimate champion.

## ✨ Key Features & Objectives

* **Data Preprocessing:** Cleaning and structuring historical international football match data to be ingested by a neural network.
* **MLP Architecture (PyTorch):** Designing a Multi-Layer Perceptron from scratch using PyTorch to handle tabular classification tasks.
* **Tournament Simulation:** Programmatically simulating the knockout stages of the World Cup to predict the semi-finalists, third-place winner, runner-up, and champion.
* **Theoretical Analysis:** Exploring the theoretical boundaries of neural networks, specifically proving the conditions under which an MLP becomes mathematically equivalent to standard Logistic Regression (i.e., having no hidden layers and utilizing a sigmoid activation function at the output).

## 📊 Results

The trained MLP model successfully simulated the Qatar 2022 World Cup brackets. Based on the learned historical patterns, the script outputs a complete prediction for the final matches, including:

* The progression of teams through the knockout stages.
* The predicted Third-Place winner.
* The predicted ultimate Champion and Runner-up of the World Cup.

