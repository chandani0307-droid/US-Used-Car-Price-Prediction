import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime
from huggingface_hub import hf_hub_download

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Download model from Hugging Face (only if needed)
model_path = hf_hub_download(
    repo_id="ckchandani0307/used-car-price-prediction-model",
    filename="best_model.pkl"
)

# Load Model
model = joblib.load(model_path)
# Load Dropdown Files
manufacturers = joblib.load(os.path.join(MODEL_DIR, "manufacturers.pkl"))
manufacturer_model = joblib.load(os.path.join(MODEL_DIR, "manufacturer_model.pkl"))
fuel_types = joblib.load(os.path.join(MODEL_DIR, "fuel_types.pkl"))
transmissions = joblib.load(os.path.join(MODEL_DIR, "transmissions.pkl"))
vehicle_types = joblib.load(os.path.join(MODEL_DIR, "vehicle_types.pkl"))
states = joblib.load(os.path.join(MODEL_DIR, "states.pkl"))

regions = joblib.load(os.path.join(MODEL_DIR, "regions.pkl"))
conditions = joblib.load(os.path.join(MODEL_DIR, "conditions.pkl"))
cylinders_list = joblib.load(os.path.join(MODEL_DIR, "cylinders.pkl"))
title_statuses = joblib.load(os.path.join(MODEL_DIR, "title_status.pkl"))
drives = joblib.load(os.path.join(MODEL_DIR, "drives.pkl"))
paint_colors = joblib.load(os.path.join(MODEL_DIR, "paint_colors.pkl"))

st.title("🚗 Used Car Price Prediction")
st.markdown("### Predict the resale price of your used car")

col1, col2 = st.columns(2)

with col1:

    manufacturer = st.selectbox(
        "Manufacturer",
        manufacturers
    )

    model_name = st.selectbox(
        "Model",
        manufacturer_model[manufacturer]
    )

    year = st.number_input(
        "Year",
        min_value=1980,
        max_value=datetime.now().year,
        value=2018
    )

    odometer = st.number_input(
        "Odometer",
        min_value=0,
        max_value=500000,
        value=50000
    )

    fuel = st.selectbox(
        "Fuel Type",
        fuel_types
    )

    region = st.selectbox(
        "Region",
        regions
    )

    condition = st.selectbox(
        "Condition",
        conditions
    )

with col2:

    transmission = st.selectbox(
        "Transmission",
        transmissions
    )

    vehicle_type = st.selectbox(
        "Vehicle Type",
        vehicle_types
    )

    state = st.selectbox(
        "State",
        states
    )

    cylinders = st.selectbox(
        "Cylinders",
        cylinders_list
    )

    drive = st.selectbox(
        "Drive",
        drives
    )

    title_status = st.selectbox(
        "Title Status",
        title_statuses
    )

    paint_color = st.selectbox(
        "Paint Color",
        paint_colors
    )

if st.button("Predict Price"):

    car_age = datetime.now().year - year
    mileage_per_year = odometer / (car_age + 1)

    luxury_brands = [
        "bmw",
        "audi",
        "lexus",
        "mercedes-benz",
        "porsche",
        "jaguar",
        "tesla",
        "land rover"
    ]

    is_luxury = 1 if manufacturer.lower() in luxury_brands else 0

    input_data = pd.DataFrame({
        "region": [region],
        "year": [year],
        "manufacturer": [manufacturer],
        "model": [model_name],
        "condition": [condition],
        "cylinders": [cylinders],
        "fuel": [fuel],
        "odometer": [odometer],
        "title_status": [title_status],
        "transmission": [transmission],
        "drive": [drive],
        "type": [vehicle_type],
        "paint_color": [paint_color],
        "state": [state],
        "car_age": [car_age],
        "mileage_per_year": [mileage_per_year],
        "is_luxury": [is_luxury]
    })

    try:
        with st.spinner("🔍 Predicting Price... Please wait..."):
            prediction = model.predict(input_data)[0]

        st.markdown("## 💰 Prediction Result")

        st.metric(
            label="Estimated Used Car Price",
            value=f"${prediction:,.2f}"
        )

    except Exception as e:
        st.error(f"❌ Prediction Failed: {e}")

# -----------------------------------
# Footer
# -----------------------------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray;">
        Made with ❤️ by <b>Chandani Kumari</b><br>
        © 2026 | US Used Car Price Prediction
    </div>
    """,
    unsafe_allow_html=True
)