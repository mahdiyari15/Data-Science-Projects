# 🔍 Task 2: Semantic Search on NiniSite (PerCQA)

## 📌 Project Overview

This task focuses on building a modern, embedding-based semantic search engine for Persian-language queries. Using the **PerCQA dataset**—which contains over 1,000 questions and 21,000 answers from the NiniSite Q&A forum—the project transitions from traditional keyword-matching techniques to a semantic retrieval system.

The pipeline includes comprehensive Natural Language Processing (NLP) for informal Persian text, Exploratory Data Analysis (EDA), vector database integration, and advanced result reranking.

## 🗂️ Dataset

* **PerCQA (NiniSite Q&A):** Provided in a JSON format (`PerCQA_JSON_Format.json`). The dataset contains rich metadata including user IDs, dates, subjects, and text bodies for both questions and comments/answers.

## ⚙️ Methodology & Pipeline

### 1. Preprocessing & Text Normalization

Informal Persian web text contains stretching, incorrect characters, and slang. The text was standardized to improve embedding quality:

* **Character Normalization:** Replaced Arabic characters (e.g., "ي", "ك") with Persian equivalents using `Hazm` and `Parsivar`.
* **Cleaning:** Removed URLs, HTML tags, punctuation, and extra spaces via regular expressions.
* **Stopword Removal & Lemmatization:** Stripped low-value words (using Hazm's stopwords) and reduced words to their dictionary roots to decrease vocabulary size.
* **Display Correction:** Utilized `arabic_reshaper` and `python-bidi` to correctly render RTL (Right-to-Left) text in charts and visualizations.

### 2. Exploratory Data Analysis (EDA)

A deep dive into community engagement and linguistic patterns:

* **Length Distributions:** Analyzed the average and median character/word counts using histograms and boxplots.
* **Activity Patterns:** Visualized user activity over time (day of the week vs. hour of the day) using time-series line charts and Seaborn heatmaps.
* **Contributor Analysis:** Identified the top 10 most active users.
* **Linguistic Analysis:** Extracted word frequencies, generated Word Clouds, and plotted the top unigrams, bigrams, and trigrams.

### 3. Vector Database & Semantic Search

Replaced traditional keyword search with a system that understands intent and context:

* **Embedding Model:** Utilized the multilingual `BAAI/bge-m3` model from Hugging Face to encode Persian question texts into 1024-dimensional dense vectors.
* **Vector Database:** Configured **LanceDB** to store schemas and efficiently query the embeddings.
* **Search Implementation:** * *Semantic Search:* Queried LanceDB using vector distance to find contextually related questions.
* *Full-Text Search (FTS):* Implemented a classical keyword-based index in LanceDB for comparison.

### 4. Advanced Answer Reranking (Bonus)

To further refine the top-$K$ results retrieved by the semantic search:

* **Cross-Encoder:** Applied the `BAAI/bge-reranker-base` model. Unlike standard embeddings that evaluate queries and documents in isolation, the reranker evaluates them as a *pair*, providing a highly accurate relevance score to re-order the final output.

## 📊 Theoretical Concepts Explored

* **Hybrid Search:** The combination of Semantic Search (capturing meaning/context) and Full-Text Search (matching exact technical terminology or names).
* **Evaluation Metrics:** Explored search ranking metrics, specifically focusing on rank-aware evaluation like Discounted Cumulative Gain (DCG) and Normalized DCG (nDCG):

$$\mathrm{DCG}_K = \sum_{i=1}^K \frac{2^{rel_i} - 1}{\log_2(i+1)}$$

$$\mathrm{nDCG}_K = \frac{\mathrm{DCG}_K}{\mathrm{IDCG}_K}$$

## 🚀 Setup & Dependencies

To run the notebook successfully, install the required packages. Because Persian text processing and local vector databases require specific libraries, use the following:

```bash
pip install pandas numpy matplotlib seaborn wordcloud tqdm
pip install hazm parsivar arabic_reshaper python-bidi
pip install lancedb transformers torch cachetools pyarrow

```

## 💻 Running the Notebook

1. Ensure `PerCQA_JSON_Format.json` is in the same directory as the notebook (or update the file path in the first cell).
2. Run the notebook sequentially.
3. The LanceDB database (`NiniSite.db`) will be generated locally in your working directory during execution.
