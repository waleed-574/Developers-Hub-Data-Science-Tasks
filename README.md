# Developers Hub Corporation - Data Science Internship Tasks

This repository contains my completed advanced data science tasks for the Developers Hub Corporation internship. 

## Repository Structure & Project Summaries

### [Task 1: Term Deposit Subscription Prediction](./Task_1_Term_Deposit/)
* **Objective:** Predict whether a bank customer will subscribe to a term deposit as a result of a marketing campaign.
* **Approach:** Trained Logistic Regression and Random Forest models using `class_weight='balanced'`. Evaluated using F1-Score and generated Explainable AI visualizations using SHAP.
* **Results:** Logistic Regression outperformed Random Forest in recalling potential subscribers (64% recall, 0.45 F1-Score). SHAP analysis identified economic indicators and previous campaign outcomes as key drivers.

### [Task 2: Customer Segmentation Using Unsupervised Learning](./Task_2_Customer_Segmentation/)
* **Objective:** Cluster mall customers based on annual income and spending habits to propose targeted marketing strategies.
* **Approach:** Conducted Exploratory Data Analysis, used the Elbow Method to find the optimal number of clusters, applied K-Means clustering, and visualized the results using PCA.
* **Results:** Identified 5 distinct customer segments (K=5), allowing for targeted strategies ranging from VIP retention for high-income/high-spenders to budget-focused promotions for lower-income groups.

### [Task 3: Energy Consumption Time Series Forecasting](./Task_3_Energy_Forecasting/)
*Note: The dataset for this task is too large to host on GitHub. To run the code, download the "Household Power Consumption" dataset from the UCI Machine Learning Repository.*
* **Objective:** Forecast short-term household energy usage using historical time-based patterns.
* **Approach:** Resampled minute-by-minute data to hourly averages. Engineered temporal features (hour, day of week, weekend). Compared ARIMA, Prophet, and XGBoost models.
* **Results:** XGBoost achieved the lowest Mean Absolute Error (0.5385). Prophet achieved the lowest Root Mean Squared Error (0.7491) by avoiding large predictive misses. Both significantly outperformed ARIMA.

### [Task 4: Loan Default Risk with Business Cost Optimization](./Task_4_Loan_Default/)
* **Objective:** Predict loan defaults and optimize the decision threshold to minimize financial loss for the business.
* **Approach:** Trained a CatBoost Classifier on credit risk data. Applied a custom business cost matrix where False Negatives (lost principal) cost 5x more than False Positives (lost interest).
* **Results:** The optimal decision threshold was found to be 0.15. This forces the model to act conservatively, minimizing the total business cost compared to the default 0.5 probability threshold.

### [Task 5: Interactive Business Dashboard in Streamlit](./Task_5_Business_Dashboard/)
* **Objective:** Develop an interactive dashboard to analyze sales, profit margins, and customer performance across a global retail dataset.
* **Approach:** Built a Python web application using Streamlit and Plotly. Implemented data caching and real-time sidebar filters for regional and category-based analysis.
* **Results:** Successfully deployed a local, interactive BI tool that recalculates KPIs (Total Sales, Profit Margin) and updates visualizations dynamically based on user inputs.