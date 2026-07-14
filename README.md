# 🚗 US Used Car Price Prediction

A Machine Learning web application that predicts the resale price of used cars in the United States using **CatBoost Regressor** and **Streamlit**.

The model is trained on a real-world Craigslist Used Cars dataset containing over **357,000+ cleaned records**. This project covers the complete Machine Learning pipeline, including data preprocessing, feature engineering, model training, evaluation, and deployment.

---

# 🌐 Live Demo

https://us-used-car-price-prediction-barvm2ybaev39ascsbhlkn.streamlit.app

---

# 📂 GitHub Repository

https://github.com/chandani0307-droid/US-Used-Car-Price-Prediction

---

# 📊 Dataset

- **Source:** Craigslist Used Cars Dataset (Kaggle)
- **Records:** 357,751
- **Features Used:** 17
- **Target Variable:** Price

Dataset Link:

https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data

---

# ✨ Features

- Data Cleaning
- Missing Value Handling
- Duplicate Removal
- Outlier Analysis
- Feature Engineering
- Exploratory Data Analysis (EDA)
- Machine Learning Model Comparison
- Interactive Streamlit Web Application
- Automatic Price Prediction
- Responsive User Interface

---

# 🤖 Machine Learning Models Compared

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- CatBoost Regressor ✅ (Final Model)

---

# 🏆 Final Model Performance

| Metric | Score |
|---------|-------|
| MAE | 2947.31 |
| RMSE | 5103.94 |
| R² Score | 0.876 |

CatBoost achieved the best performance and was selected as the final deployment model.

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- CatBoost
- Streamlit
- Joblib
- Hugging Face
- GitHub

---

# 📁 Project Structure

```
US-Used-Car-Price-Prediction/
│
├── app/
│   └── app.py
│
├── models/
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
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

> **Note:** The trained CatBoost model (`best_model.pkl`) is hosted on **Hugging Face** because it exceeds GitHub's file size limit.

---

# ▶️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/chandani0307-droid/US-Used-Car-Price-Prediction.git
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit Application

```bash
streamlit run app/app.py
```

---

# 📷 Web Application

The Streamlit application allows users to:

- Select Manufacturer
- Select Car Model
- Enter Vehicle Details
- Predict Used Car Price Instantly
- Get Real-Time Estimated Price

---

# 🔮 Future Improvements

- Support Indian Used Car Dataset
- Add Car Image Upload
- Price Trend Visualization
- Model Explainability using SHAP
- Better UI/UX
- Docker Deployment
- REST API using FastAPI

---

# 👩‍💻 Author

**Chandani Kumari**

AI & Data Science Student

GitHub:

https://github.com/chandani0307-droid

---

⭐ **If you found this project useful, please consider giving it a Star on GitHub!**