# 🧠 Task 3: Large Language Models for Multiple-Choice Reasoning

## 📌 Project Overview

Traditional machine learning models (like classification or regression) can struggle with tasks that require deep semantic understanding and nuanced reasoning. This task explores the capabilities of foundation models—specifically **BERT** (`bert-base-uncased`)—to solve complex multiple-choice questions (MCQs).

Using the **SWAG (Situations With Adversarial Generations)** dataset, this project evaluates the baseline performance of a pre-trained model and systematically improves it through **In-Context Learning (ICL)**, **Parameter-Efficient Fine-Tuning (PEFT) using LoRA**, and a combination of both approaches.

## 🗂️ Dataset

* **SWAG (`regular` split):** A dataset of over 113,000 multiple-choice questions based on real-world scenarios. Each example consists of a context (a starting situation) and four possible endings, demanding commonsense reasoning to pick the most plausible continuation.

## ⚙️ Methodology & Pipeline

### 1. Exploratory Data Analysis & Preprocessing

To prepare the dataset for a multiple-choice architecture:

* **EDA:** Visualized the label distribution (which proved to be uniformly distributed) and the exponential-shaped length distribution of both contexts and endings.
* **Formatting:** Duplicated the context four times per example and concatenated each with one of the four candidate endings to create four distinct sequence pairs per question.
* **Tokenization & Padding:** Processed sequences using the `AutoTokenizer` and employed `DataCollatorForMultipleChoice` for dynamic padding. This ensures sequences are only padded to the maximum length of their specific batch, optimizing memory and computation.

### 2. Baseline Evaluation

Tested the raw, off-the-shelf `bert-base-uncased` model using the validation split.

* **Observation:** The baseline accuracy was incredibly low (around 13%), demonstrating that without task-specific context or fine-tuning, the model performs worse than random guessing on these adversarial questions.

### 3. In-Context Learning (ICL)

To unlock the model's reasoning abilities without updating its weights, three ICL techniques were implemented by restructuring the input prompts:

* **Few-Shot Learning:** Prepended 4 randomly selected example Q&A pairs (one for each label) to the prompt.
* **Zero-Shot Reasoning (Chain of Thought):** Appended the phrase *"Let's think step by step."* to the context to encourage sequential logic.
* **Instruction Tuning:** Added an explicit system-like instruction (*"Read the question and choose the most plausible ending."*) before the context.

### 4. Parameter-Efficient Fine-Tuning (LoRA)

To adapt the model to the specific structure of the SWAG dataset while overcoming hardware limitations (e.g., Kaggle GPU memory constraints):

* **LoRA Setup:** Applied Low-Rank Adaptation (`r=8`, `lora_alpha=16`) to train only a small fraction of the model's parameters.
* **Training Arguments:** Utilized **Gradient Accumulation** (8 steps) to simulate a larger batch size, `FP16` precision for speed, and a learning rate of `2e-5` over 2 epochs.
* **Metrics:** Developed custom evaluation functions to calculate **Accuracy** and **Perplexity** (via negative log-likelihood) to measure model confidence.

### 5. Combined Approach

Finally, the project evaluates whether a model that has *already* been fine-tuned (LoRA) can still benefit from In-Context Learning (Few-Shot prompts). The results before and after were compared using standard classification reports and confusion matrices.

## 📊 Key Results & Evaluation Metrics

* **Accuracy:** Tracked the percentage of correct answers across Baseline, ICL, Fine-Tuned, and Combined states. Fine-tuning showed the most massive leap in performance.
* **Perplexity:** Used during the fine-tuning evaluation to measure how confident the model was in its correct predictions (lower is better).
* **Confusion Matrix:** Plotted via `sklearn` and `matplotlib` to visually diagnose if the fine-tuned model struggled with specific candidate positions (0, 1, 2, or 3).

## 🚀 Setup & Installation

**Prerequisites:**
You will need a Hugging Face account and an Access Token to download the dataset and models. Ensure you have Python 3.8+ and a GPU-enabled environment.

```bash
pip install torch transformers datasets evaluate peft scikit-learn matplotlib seaborn tqdm

```

**Running the Code:**

1. Insert your Hugging Face token in the script where `login(token="YOUR_TOKEN_HERE")` is called.
2. Run the notebook sequentially.
