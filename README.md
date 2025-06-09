# 🏠 House Price Prediction in Tunisia

This project focuses on building a machine learning pipeline to predict real estate prices in Tunisia using data scraped from [Tayara.tn](https://www.tayara.tn). The goal is to estimate property prices (in TND) based on features such as property type, surface area, number of bedrooms and bathrooms, and location.

---

## 🕸️ Web Scraping

- Data was scraped from Tayara.tn using **BeautifulSoup** in Python.
- Extracted fields included:
  - `Title`
  - `Price`
  - `Type`
  - `Area`
  - `Localisation`
  - `#Bedrooms`
  - `#Bathrooms`

---

## 🧼 Data Cleaning

- Removed unrealistic price entries.
- Imputed missing values using a combination of:
  - **KNN Imputer** (for categorical and numerical fields)
  - **Median imputation** (for area and bedrooms)
  - **Mode imputation** (for bathrooms based on type and location)
- Dropped outliers and irrelevant columns.

📝 You can find **data visualizations before and after cleaning** in the following reports generated with `ydata_profiling`:
- [`data/immobiliers_report_before_cleaning.html`](data/immobiliers_report_before_cleaning.html)
- [`data/immobiliers_report_after_cleaning.html`](data/immobiliers_report_after_cleaning.html)

---

## 🧠 Feature Engineering

Several new features were engineered to improve model performance:

- `Area_x_Bathrooms` (interaction term: Area × Bathrooms)
- `Log_Area` and `Log_Price` (log-transformed features to handle skewed distributions)
- `Bathrooms_per_Bedroom` (ratio feature)

⚠️ Features derived directly from the target, such as `Price_per_m2`, were excluded to prevent data leakage.

---

## 🔧 Modeling Pipeline

The machine learning pipeline was built using **PyCaret**, which automates:

- Imputation
- Encoding of categorical variables
- Feature scaling
- Dimensionality reduction (PCA)
- Feature selection
- Model training and evaluation

📎 _Pipeline overview:_  
![Pipeline](data/pipeline_plot.png)

---

## 💻 Tech Stack

- Python 3.9+
- ydata_profiling (ProfileReport)
- BeautifulSoup 4
- Pandas & NumPy
- Scikit-learn
- PyCaret (regression module)

---
