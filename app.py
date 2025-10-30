import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('best_energy_efficiency_model.pkl')

st.title("Energy Efficiency Heating Load Predictor")

st.write("Enter building feature values:")

# Input fields for features (adjust according to your feature names)
relative_compactness = st.number_input('Relative Compactness', min_value=0.0, max_value=10.0, value=0.8)
surface_area = st.number_input('Surface Area', min_value=0.0, max_value=1000.0, value=600.0)
wall_area = st.number_input('Wall Area', min_value=0.0, max_value=1000.0, value=300.0)
roof_area = st.number_input('Roof Area', min_value=0.0, max_value=1000.0, value=250.0)
overall_height = st.number_input('Overall Height', min_value=0.0, max_value=20.0, value=7.0)
orientation = st.selectbox('Orientation', options=[2,3,4,5])  # example categories
glazing_area = st.number_input('Glazing Area', min_value=0.0, max_value=1.0, value=0.1)
glazing_area_dist = st.selectbox('Glazing Area Distribution', options=[0,1,2,3,4,5])

# Make prediction button
if st.button('Predict Heating Load'):
    # Prepare input array
    input_data = np.array([[relative_compactness, surface_area, wall_area, roof_area,
                            overall_height, orientation, glazing_area, glazing_area_dist]])
    # Scale or preprocess input as you did for training (if needed)
    # For example, if you used StandardScaler, load and apply the scaler here
    
    prediction = model.predict(input_data)
    st.success(f'Predicted Heating Load: {prediction[0]:.2f}')
