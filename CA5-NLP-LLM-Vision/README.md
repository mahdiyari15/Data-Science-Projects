#  Advanced Data Science: NLP, LLMs, and Computer Vision

## 📌 Project Overview

This repository contains the implementations for four advanced data science tasks (Assignments 5 & 6). Spanning multiple domains—including natural language processing (NLP), computer vision, and semi-supervised learning—this project explores both traditional machine learning techniques and the capabilities of modern foundation models (LLMs) to tackle real-world, data-scarce challenges.

## 📂 Task Breakdown

### 🎮 Task 1: Video Game Review Score Prediction (Semi-Supervised Learning)

Focuses on predicting numerical review scores (1-10) using limited labeled data and a large pool of unlabeled text.

* **Key Concepts:** Semi-supervised learning (Pseudo-Labeling) and Active Learning strategies.

* **Techniques:** Sentence Transformers, Word2Vec embeddings, PCA dimensionality reduction, and XGBoost classification/regression models.

### 🔍 Task 2: Semantic Search on NiniSite (Persian NLP)

Guides the development of an intelligent search engine for Persian-language Q&A data.

* **Key Concepts:** Embedding-based retrieval, vector databases, and result reranking.

* **Techniques:** Text normalization (Hazm/Parsivar), LanceDB vector storage, `bge-m3` embeddings, and Cross-Encoder reranking models.

### 🧠 Task 3: LLMs for Multiple-Choice Reasoning (SWAG Dataset)

Highlights the limitations of classical modeling techniques by utilizing large language models for complex multiple-choice reasoning on the SWAG dataset.

* **Key Concepts:** Prompt engineering, zero-shot/few-shot prompting, and parameter-efficient adaptation.

* **Techniques:** BERT (`bert-base-uncased`), In-Context Learning (ICL), and LoRA (Low-Rank Adaptation) fine-tuning.

### ⚽ Task 4: Unsupervised Image Segmentation

Tackles the challenge of pixel-level image segmentation without labeled training data by isolating football players in match footage.

* **Key Concepts:** Unsupervised computer vision and pixel clustering.

* **Techniques:** K-Means, DBSCAN, Agglomerative Clustering, hand-crafted features (Sobel, LBP), deep features (HRNet), and evaluation using IoU and Dice coefficients.

## 🛠️ Technologies & Libraries Used

* **Machine Learning & Deep Learning:** `scikit-learn`, `xgboost`, `torch`, `torchvision`, `timm`, `peft`
* **NLP & Embeddings:** `transformers`, `sentence-transformers`, `gensim`, `nltk`, `hazm`, `parsivar`
* **Computer Vision:** `opencv-python` (`cv2`), `scikit-image`
* **Databases & Data Manipulation:** `lancedb`, `pandas`, `numpy`, `datasets`

