

# 🎮 Task 1: Video Game Review Score Prediction

## 📌 Overview

This project tackles the challenge of predicting video game review scores (ranging from 1 to 10) based on short textual summaries. In real-world scenarios, obtaining human-assigned scores for massive amounts of text is expensive and time-consuming. To simulate this, the project utilizes a small **labeled dataset** alongside a large **unlabeled dataset**.

The primary objective is to build robust prediction models by establishing supervised baselines and subsequently employing **Semi-Supervised Learning (SSL)** and **Active Learning** techniques to leverage the vast pool of unlabeled data.

## 🗂️ Dataset

* **`labeled-data.csv`**: Contains `review_text` and `review_score` (1-10). Represents the limited annotation budget.
* **`unlabeled-data.csv`**: Contains only `review_text`. Represents the large pool of raw data used to enhance model generalization.

## 🚀 Project Pipeline & Methodology

### 1. Text Vectorization

To transform the raw textual reviews into machine-readable numerical formats, two distinct embedding strategies were implemented:

* **Sentence Transformers (Semantic):** Utilized the pre-trained `all-MiniLM-L6-v2` model to capture deep semantic meaning, exporting dense vector embeddings.
* **Word2Vec (Syntactic/Contextual):** Trained a custom Word2Vec model using `Gensim` on the combined corpus. Sentence embeddings were derived by averaging the constituent word vectors.
* **Dimensionality Reduction:** Applied **PCA** to reduce embeddings to 2D space for visualization, helping to identify underlying clusters and class separability.

### 2. Supervised Learning Baselines

Before applying advanced techniques, baseline models were trained strictly on the labeled dataset. Classes with fewer than 10 samples were filtered out to ensure statistical reliability.

* **Classification Paradigm:** Treated scores as discrete categories. Models tested: `Logistic Regression`, `Random Forest Classifier`, `SVC`.
* **Regression Paradigm:** Treated scores as continuous values. Models tested: `Linear Regression`, `Random Forest Regressor`, `SVR`.
* *Evaluation Metrics:* Accuracy, Precision, Recall, F1-Score, MAE, MSE, RMSE, and R².

### 3. Semi-Supervised Learning (SSL) Strategies

To capitalize on the unlabeled data, we utilized `XGBoost` (Classifier and Regressor) to apply two advanced learning strategies:

* **Pseudo-Labeling:**
* **Concept:** The model predicts labels for the unlabeled pool. The top 1% most confident predictions are accepted as "pseudo-labels" and added to the training set for the next iteration.
* **Implementation:** Executed for both Classification (using prediction probabilities) and Regression (using confidence derived from deviation from the mean).

* **Active Learning:**
* **Concept:** The algorithm strategically selects the most "informative" or "uncertain" samples from the unlabeled pool to be manually labeled (simulated).
* **Classification Strategies:** `Margin Sampling`, `Entropy-Based Sampling`, and `Least Confidence`.
* **Regression Strategy:** Local uncertainty estimation using K-Nearest Neighbors (KNN) variance.

### 4. Evaluation & Comparative Analysis

The performance of the models across iterations was meticulously tracked and visualized:

* **Learning Curves:** Tracking Accuracy/F1 for classification and RMSE/MAE/R² for regression across iterations.
* **ROC & AUC:** Plotted multi-class ROC curves (One-vs-Rest) and computed Macro-AUC to evaluate the model's ability to distinguish between score classes.
* **Metrics Tracking:** All iterative metrics and generated pseudo-labels were exported to CSVs for further analysis.

## 🛠️ Setup & Installation

**Prerequisites:**
Ensure you have Python 3.8+ installed. You will need the following libraries:

```bash
pip install pandas numpy scikit-learn xgboost nltk sentence-transformers gensim matplotlib

```

## 📁 Generated Outputs

Upon running the script, the following files will be generated in your working directory:

* **Embeddings:** `labeled_embeddings_ST.csv`, `unlabeled_embeddings_ST.csv`, `labeled_embeddings_W2V.csv`, `unlabeled_embeddings_W2V.csv`
* **Pseudo-Labeling Logs:** `pseudo_labels_XGB.csv`, `metrics_XGB.csv`, `pseudo_labels_regression.csv`, `metrics_regression.csv`
* **Active Learning Logs:** `active_learning_entropy_metrics.csv`, `active_learning_margin_metrics.csv`, `active_learning_least_conf_metrics.csv`, `regression_active_learning_metrics.csv`
