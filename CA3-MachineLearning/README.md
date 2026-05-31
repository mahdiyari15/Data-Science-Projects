# Machine Learning Applications: Classification, Regression, and Recommendation
The project tackles three distinct real-world machine learning challenges using traditional (non-deep learning) algorithms. Each task was developed as part of an academic Kaggle competition.

## 📖 Overview

The primary objective of this project is to apply data preprocessing, feature engineering, and traditional machine learning models to solve three different types of problems:

1. **Classification:** Predicting cancer patient survival status.
2. **Regression:** Forecasting daily bike rental demand.
3. **Recommendation System:** Predicting user ratings for movies.

*Note: Per the project constraints, no deep learning or pre-trained neural networks were used; all solutions rely strictly on traditional machine learning algorithms.*

## 🎯 Main Objectives & Tasks

### Task 1: Cancer Survival Prediction (Binary Classification)

* **Goal:** Develop a binary classification model to predict the survival status of cancer patients.
* **Data:** Patient demographics, medical history (e.g., Cancer Type, Tumor Size, Treatment Details).
* **Approach:** Implemented data preprocessing to handle missing values and categorical features, and utilized ensemble methods like `RandomForestClassifier` and `XGBClassifier` (combined via `VotingClassifier`) to maximize predictive accuracy.

### Task 2: Bike Rental Forecasting (Regression)

* **Goal:** Build a regression model to predict the total number of casual and registered bike rentals on a given day.
* **Data:** Environmental and seasonal features such as temperature, weather conditions, holidays, and humidity.
* **Approach:** Applied regularization techniques including `Ridge` and `Lasso` regression to predict continuous demand while avoiding overfitting. Evaluated models using Mean Squared Error (MSE).

### Task 3: Movie Recommendation System

* **Goal:** Design a recommendation system to accurately predict how a specific user will rate a specific movie.
* **Data:** User-item rating matrices (`train_data_movie_rate.csv`) and user trust networks (`train_data_movie_trust.csv`).
* **Approach:** Built a predictive model combining collaborative filtering concepts with tree-based regression algorithms like `RandomForestRegressor` to estimate user ratings on a scale (clipped between 0.5 and 4.0).

## 🛠️ Tech Stack

* **Language:** Python 3
* **Machine Learning Libraries:** `scikit-learn`, `xgboost`
* **Data Processing:** `pandas`, `numpy`
* **Evaluation Metrics:** Accuracy (Task 1), Mean Squared Error / MSE (Task 2), Mean Absolute Error / MAE (Task 3)

