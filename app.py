# app.py - Laptop Price Predictor
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------
# Load model and columns
# -------------------
model = pickle.load(open('model.pkl', 'rb'))
X_columns = pickle.load(open('X_columns.pkl', 'rb'))

# -------------------
# App title
# -------------------
st.set_page_config(page_title="Laptop Price Predictor", layout="wide")
st.title("💻 Laptop Price Predictor")
st.write("This app predicts laptop prices based on hardware specifications.")
st.write("App-kan wuxuu saadaalinayaa qiimaha laptop-ka iyadoo lagu saleynayo specs-ka.")

# -------------------
# Sidebar Inputs
# -------------------
company = st.sidebar.selectbox("Company / Brand", sorted([
    'Apple','Asus','Chuwi','Dell','Fujitsu','Google','HP','Huawei','LG','Lenovo','MSI',
    'Mediacom','Microsoft','Razer','Samsung','Toshiba','Vero','Xiaomi'
]))

product = st.sidebar.selectbox("Product", sorted([
    'Product_14-am079na', 'Product_15-AC110nv', 'Product_15-AY023na', 'Product_15-BA015wm'
]))

type_name = st.sidebar.selectbox("Type Name", ['Gaming','Notebook','Ultrabook','Netbook','Workstation'])

screen_res = st.sidebar.selectbox("Screen Resolution", [
    '1366x768','1440x900','1600x900','1920x1080','2560x1440','3840x2160'
])

cpu = st.sidebar.selectbox("CPU", [
    'Intel Core i3','Intel Core i5','Intel Core i7',
    'AMD A9','AMD A10','AMD Ryzen 5','AMD Ryzen 7'
])

ram = st.sidebar.slider("RAM (GB)", 2, 64, 8)
weight = st.sidebar.slider("Weight (kg)", 1.0, 5.0, 2.0)
inches = st.sidebar.slider("Screen Size (inches)", 10.0, 20.0, 15.6)

# -------------------
# Prepare input for prediction
# -------------------
if st.sidebar.button("Predict Price 💰"):
    # Create empty dataframe
    input_data = pd.DataFrame(columns=X_columns)
    input_data.loc[0] = 0  # Initialize with zeros

    # Fill in user inputs
    features = {
        f'Company_{company}': 1,
        f'Product_{product}': 1,
        f'TypeName_{type_name}': 1,
        f'ScreenResolution_{screen_res}': 1,
        f'Cpu_{cpu}': 1,
        'Ram': ram,
        'Weight': weight,
        'Inches': inches
    }

    # Only fill columns that exist in X_columns
    for col, val in features.items():
        if col in input_data.columns:
            input_data.at[0, col] = val

    # Make prediction
    price_pred = model.predict(input_data)[0]
    st.success(f"💸 Predicted Laptop Price: ${round(price_pred, 2)}")

