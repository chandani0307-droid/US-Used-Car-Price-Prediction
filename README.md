# 🚗 Used Car Price Prediction

## 📌 Project Overview

This project predicts the resale price of used cars using Machine Learning.

The model is trained on a real-world Craigslist Used Cars dataset containing over **357,000+ cleaned records**. The project includes complete data preprocessing, exploratory data analysis (EDA), feature engineering, model comparison, and deployment using Streamlit.

---

## 📂 Dataset

- **Source:** Craigslist Used Cars Dataset
- **Total Records:** 357,751
- **Features Used:** 17
- **Target Variable:** Price

---

## 🚀 Features

- Data Cleaning
- Missing Value Handling
- Duplicate Removal
- Outlier Analysis
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Machine Learning Model Comparison
- Interactive Streamlit Web Application

---

## 🤖 Models Compared

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- CatBoost Regressor ✅ (Final Model)

---

## 🏆 Final Model Performance

| Metric | Score |
|---------|-------|
| MAE | 2947.31 |
| RMSE | 5103.94 |
| R² Score | 0.876 |

CatBoost achieved the best performance and was selected as the final model for deployment.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- CatBoost
- Streamlit
- Joblib

---

## 📁 Project Structure

```
Used-Car-Price-Prediction/
│
├── app/
│   └── app.py
│
├── models/
│   ├── best_model.pkl
│   ├── manufacturers.pkl
│   ├── manufacturer_model.pkl
│   ├── fuel_types.pkl
│   ├── transmissions.pkl
│   ├── vehicle_types.pkl
│   ├── states.pkl
│   ├── regions.pkl
│   ├── conditions.pkl
│   ├── cylinders.pkl
│   ├── title_status.pkl
│   ├── drives.pkl
│   └── paint_colors.pkl
│
├── notebooks/
├── data/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-link>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app/app.py
```

---

## 📷 Application

The Streamlit application allows users to:

- Select manufacturer and model
- Enter vehicle details
- Predict the estimated resale price instantly

---

## 🔮 Future Improvements

- Add car image upload for prediction.
- Improve user interface and user experience.
- Add model explainability using SHAP.
- Optimize the model for faster predictions.

---

## 👩‍💻 Author

**Chandani Kumari**

AI & SData Science Student

---

⭐ If you found this project useful, consider giving it a star on GitHub.