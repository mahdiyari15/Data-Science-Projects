# Statistical Inference and Simulations in Data Science

This repository contains the implementation of key statistical concepts essential for analyzing data, making inferences, and drawing conclusions. The project is structured around three real-world data science scenarios focusing on probability, Monte Carlo simulations, and hypothesis testing.

##  Main Objectives

1. **Roulette Simulation and Profit Analysis:** Simulate American Roulette to analyze the expected outcomes and profit distributions for a player. Compare theoretical mathematical expectations with Monte Carlo simulated results.
2. **2016 USA Presidential Election Prediction:** Analyze and aggregate polling data to predict the election outcome. Use the Central Limit Theorem (CLT) to estimate the true proportion of voters and calculate the confidence interval of the spread.
3. **Drug Safety Testing:** Perform data preprocessing and statistical hypothesis testing on clinical trial data to evaluate the significance of adverse effects and blood cell counts between patients receiving a drug versus a placebo.

## Core Concepts Explored

* **Probability & Expected Value:** Calculating theoretical win rates and expected returns.
* **Monte Carlo Simulations:** Approximating probability distributions and verifying theories through high-volume random sampling.
* **Central Limit Theorem (CLT):** Computing standard errors and 95% Confidence Intervals (CI).
* **Hypothesis Testing:** Utilizing Z-scores, p-values, and Two-Sample Independent T-tests (e.g., `scipy.stats.ttest_ind`) to accept or reject null hypotheses.

## Key Results

* **Roulette Simulation:** Simulations verified that while short-term outcomes vary, the expected value of a player's profit is negative in the long run. As the number of rounds ($N$) increases, the distribution of total profits normalizes (via CLT), and the probability of the casino losing money rapidly approaches 0.
* **Election Polling Analysis:** Derived a 95% Confidence Interval for the true proportion of voters, which was validated to capture the true proportion in $\approx 95\%$ of Monte Carlo iterations. Hypothesis testing (using both p-values and confidence intervals) successfully rejected the null hypothesis ($H_0$), proving a statistically significant difference between the Clinton-Trump vote spread and 0.
* **Drug Safety Test:** Successfully cleaned the trial dataset (handling missing `NaN` values) and extracted core descriptive statistics. Applied robust two-sided independent T-tests to determine whether the differences observed in patient metrics between the treatment and control groups were statistically significant.

## Tech Stack

* **Language:** Python 3
* **Libraries:** `pandas` (Data manipulation), `numpy` (Numerical computing), `scipy.stats` (Statistical functions & distributions), `matplotlib` (Data visualization)