import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('Demo: Loading Uber Pickup Data in NYC with Caching')



DATE_COLUMN = 'Date/Time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
local_data = 'dataset/Kaggle_Training_Dataset_v2.csv'
@st.cache_data
def load_data(nrow):
    ### Simulating Loading a Large Dataset
    data = pd.read_csv(local_data, nrows=nrow)

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

data_load_state = st.text('Stand by...')
data = load_data(1000)
data_load_state.text('Complete!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.markdown(
    """
Description:

- sku – Random ID for the product
- national_inv – Current inventory level for the part
- lead_time – Transit time for product (if available)
- in_transit_qty – Amount of product in transit from source
- forecast_3_month – Forecast sales for the next 3 months
- forecast_6_month – Forecast sales for the next 6 months
- forecast_9_month – Forecast sales for the next 9 months
- sales_1_month – Sales quantity for the prior 1 month time period
- sales_3_month – Sales quantity for the prior 3 month time period
- sales_6_month – Sales quantity for the prior 6 month time period
- sales_9_month – Sales quantity for the prior 9 month time period
- min_bank – Minimum recommend amount to stock
- potential_issue – Source issue for part identified
- pieces_past_due – Parts overdue from source
- perf_6_month_avg – Source performance for prior 6 month period
- perf_12_month_avg – Source performance for prior 12 month period
- local_bo_qty – Amount of stock orders overdue
- deck_risk – Part risk flag
- oe_constraint – Part risk flag
- ppap_risk – Part risk flag
- stop_auto_buy – Part risk flag
- rev_stop – Part risk flag
- went_on_backorder – Product actually went on backorder
"""
)