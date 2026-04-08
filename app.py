import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('models/model.pkl', 'rb'))

st.title("📊 Customer Segmentation (Clustering App)")
st.write("Enter customer details below:")
# Load original dataset structure
df = pd.read_csv('data/mall_customers.csv')

# Keep only numeric columns (same as training)
X = df.select_dtypes(include=['int64', 'float64'])

# Create empty input with same columns
input_df = pd.DataFrame(columns=X.columns)

# Fill values (adjust based on columns)
for col in X.columns:
    input_df.loc[0, col] = st.number_input(f"{col}", value=0.0)

# Predict
if st.button("Predict Cluster"):
    prediction = model.predict(input_df)
    st.success(f"Cluster: {prediction[0]}")