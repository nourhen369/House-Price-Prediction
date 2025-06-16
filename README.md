# 🏠 House Price Prediction in Tunisia

This project focuses on building a machine learning pipeline and deployment stack to predict real estate prices in Tunisia using data scraped from [Tayara.tn](https://www.tayara.tn). The goal is to estimate property prices (in TND) based on features such as property type, surface area, number of bedrooms and bathrooms, and location.

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

Features derived directly from the target, such as `Price_per_m2`, were excluded to prevent data leakage.

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

Final model was built using **XGBoost** and **scikit-learn**, independently of PyCaret and persisted with `joblib`.

---

## 🚀 Deployment

- **API:** FastAPI serves the trained model for prediction.
- **Web Interface:** Streamlit provides a simple user interface to input features and get predictions.
- **Containerization:** Docker is used to containerize the application for easy deployment.
- **Cloud:** Infrastructure as Code (IaC) with Terraform and Ansible to provision and configure an Azure VM, install Docker, and deploy the container.

---

## 🗂️ Project Structure

```
.
├── app/
│   ├── main.py         # FastAPI backend
│   ├── front.py        # Streamlit frontend
│   ├── House.py        # House data model
├── model/
│   ├── data/           # Contains visualisations before and after cleaning
│   ├── 1-scrapping.ipynb         
│   ├── 2-viz-and-cleaning.ipynb         
│   ├── 3-modeling.ipynb         
│   └── xgboost_model.pkl
├── infra/
│   ├── main.tf         # Terraform configuration
│   ├── deploy.yml      # Ansible playbook
│   └── inventory.ini   # Ansible inventory
├── requirements.txt
├── Dockerfile
├── start.sh
└── README.md
```
---