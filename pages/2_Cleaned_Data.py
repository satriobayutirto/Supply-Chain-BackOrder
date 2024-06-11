import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Cleaned Data')



cleaned_data = 'dataset/cleaned_dataset.csv'
@st.cache_data
def load_data(nrow):
    ### Simulating Loading a Large Dataset
    data = pd.read_csv(cleaned_data, nrows=nrow)

    chunk_1 = data[0:200]
    chunk_2 = data[200:400]
    chunk_3 = data[400:600]
    chunk_4 = data[600:800]
    chunk_5 = data[800:]

    all_chunk = [chunk_1, chunk_2, chunk_3, chunk_4, chunk_5]

    new_data = pd.DataFrame()
    counter_text = st.text('Processing...')
    for i, chunk in enumerate(all_chunk):
        counter_text.text(f"Processing Part {i+1}/{len(all_chunk)}")
        time.sleep(0.6)
        new_data = new_data.append(chunk).reset_index(drop = True)
    del counter_text
    
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Stand By...')
data = load_data(1000)
data_load_state.text('Complete!')

if st.checkbox('Show Cleaned data'):
    st.subheader('Cleaned data')
    st.write(data)

st.markdown(
    """
    **New Feature:**
    
   - sales_trend_1_to_3 : Trend selling
   - in_transit_to_inventory : Ratio from transit and national inventory
   - avg_performance' : Average from combine performance 6 and 12 month
   - Demand Variability: Average sales
   - LTD : Lead Time Demand 
    """
)