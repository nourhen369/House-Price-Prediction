import streamlit as st
import requests

st.title("House Price Prediction")

# User input fields
region = st.selectbox("Region", [
    'Ariana', 'Nabeul', 'La Manouba', 'Ben Arous', 'Bizerte', 'Tunis', 'Sfax',
    'Monastir', 'Sousse', 'Zaghouan', 'Médenine', 'Gafsa', 'Béja', 'Jendouba',
    'Le Kef', 'Kairouan', 'Gabès', 'Mahdia', 'Siliana', 'Sidi Bouzid', 'Tozeur',
    'Kasserine'
])
type_ = st.selectbox("Type", ['Appartement', 'Villa'])
area = st.number_input("Area (m²)", min_value=1.0, value=100.0)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, value=1)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, value=1)

if st.button("Predict"):
    # Prepare data for API
    data = {
        "Region": region,
        "Type": type_,
        "Area": area,
        "Bathrooms": bathrooms,
        "Bedrooms": bedrooms
    }
    # Call FastAPI endpoint
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    if response.status_code == 200:
        st.success(f"Predicted Price: {response.json()['predicted_price'] * 1.2:,.0f} TND")
    else:
        st.error(f"Error: {response.json()['detail']}")