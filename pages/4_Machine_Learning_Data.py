import streamlit as st
import pandas as pd
import numpy as np

import joblib

st.title('Model Prediction')

st.markdown(""" Prerequisite:
    - You have to save a usable model first
    - Your saved model is accessible from the directory of this project """)

model_option = st.selectbox(
    "Choose a model to use for prediction:",
    ("Random Forest", "XGBoost")
)

@st.cache_data
def load_model():
    if model_option== "Random Forest":
        return joblib.load(open('model/RF_BackOrder.pkl', 'rb'))
    else:
        return joblib.load(open('model/XGB_BackOrder.pkl', 'rb'))




def process_input(input_data):
    feature_mapping = {
        'National Inventory': 'national_inv',
        'Lead Time': 'lead_time',
        'In Transit Quantity': 'in_transit_qty',
        'Minimum Bank': 'min_bank',
        'Pieces Past Due': 'pieces_past_due',
        'Local Back Order Quantity': 'local_bo_qty',
        'Sales Trend (1 to 3)': 'sales_trend_1_to_3',
        'Sales Trend (3 to 6)': 'sales_trend_3_to_6',
        'Sales Trend (6 to 9)': 'sales_trend_6_to_9',
        'In Transit to Inventory': 'in_transit_to_inventory',
        'Average Performance': 'avg_performance',
        'Demand Variability': 'demand_variability',
        'LTD': 'LTD',
        'Potential Issue': 'potential_issue_Yes',
        'Deck Risk': 'deck_risk_Yes',
        'OE Constraint': 'oe_constraint_Yes',
        'PPAP Risk': 'ppap_risk_Yes',
        'Stop Auto Buy': 'stop_auto_buy_Yes',
        'Rev Stop': 'rev_stop_Yes'
    }
    input_data = input_data.rename(columns=feature_mapping)
    # Memisahkan fitur numerik dari fitur boolean
    numeric_features = input_data[['national_inv', 'lead_time', 'in_transit_qty', 'min_bank', 'pieces_past_due', 'local_bo_qty', 'sales_trend_1_to_3', 'sales_trend_3_to_6', 'sales_trend_6_to_9', 'in_transit_to_inventory', 'avg_performance', 'demand_variability', 'LTD']]
    boolean_features = input_data[[ 'potential_issue_Yes',
 'deck_risk_Yes',
 'oe_constraint_Yes',
 'ppap_risk_Yes',
 'stop_auto_buy_Yes',
 'rev_stop_Yes']]

    # Memuat model
    model = load_model()
    scaler = joblib.load('model/scaler.pkl')
    
    
    
    # Gabungkan fitur numerik yang telah distandarisasi dengan fitur boolean
    input_data = np.hstack((numeric_features, boolean_features))
    
    # Standarisasi data numerik
    input_scaled = scaler.transform(input_data)
    
    # Memprediksi data
    prediction = model.predict(input_scaled)
    
    return prediction

def convert_to_back_order(prediction):
    return "Yes" if prediction == 1 else "No"

st.subheader("Fill requitment information")
# Tabel input
st.write("## Input Table")

# Kolom input numerik
input_data = {}
for col in ['National Inventory', 'Lead Time', 'In Transit Quantity', 'Minimum Bank', 'Pieces Past Due', 'Local Back Order Quantity', 'Sales Trend (1 to 3)', 'Sales Trend (3 to 6)', 'Sales Trend (6 to 9)', 'In Transit to Inventory', 'Average Performance', 'Demand Variability']:
    input_data[col] = st.number_input(f"Enter value for {col}", step=1)

# Hitung nilai LTD
input_data['LTD'] = input_data['Demand Variability'] * input_data['Lead Time']

# Kolom input boolean
st.write("## Click True or False")
boolean_data = {}
for col in [ 'Potential Issue', 'Deck Risk', 'OE Constraint', 'PPAP Risk', 'Stop Auto Buy', 'Rev Stop']:
    boolean_data[col] = st.radio(f"Is {col}?", ('Yes', 'No')) == 'Yes'

# Gabungkan tabel input numerik dan boolean
input_df = pd.DataFrame([input_data])
input_df = pd.concat([input_df, pd.DataFrame([boolean_data])], axis=1)


# Ketika tombol ditekan
if st.button('Predict'):
    # Proses input dan prediksi
    prediction = process_input(input_df)
    
    prediction_label = convert_to_back_order(prediction)
    # Tampilkan prediksi
    st.write("### Back Order Prediction")
    st.write(prediction_label)
