import streamlit as st
import pandas as pd
import numpy as np
import time

import folium
import branca.colormap as cm
from streamlit_folium import folium_static
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title('Visualizing')

st.markdown(
    """
    BackOrder Visualization
    """
)

df = pd.read_csv('dataset/cleaned_dataset.csv')

# @st.cache_data
# def show_data():
#     features = [
#         'national_inv',
#         'demand_variability'
#     ]
    
#     #Membuat subplot boxplot menggunakan Plotly
#     fig = make_subplots(rows=1, cols=len(features), subplot_titles=features)

#     for i, feature in enumerate(features):
#         fig.add_trace(
#             go.Box(y=df[feature], name=feature, marker_color='red', boxpoints='all', notched=True),
#             row=1, col=i+1
#         )

#     #Menyesuaikan layout
#     fig.update_layout(height=600, width=1800, title_text="Boxplot for Numerical Features")
#     st.plotly_chart(fig)
#     st.write(df)

# show_data()
#Error Data Exceed 248,7MB size limit 200MB

st.subheader('Need BackOrder')

@st.cache_data
def visualize_boxplot():
    tab1, tab2 = st.tabs(['Demand', 'National inv'])
    with tab1:
        fig = px.box(df, x='went_on_backorder', y='demand_variability')
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    with tab2:
        fig = px.box(df, x='went_on_backorder', y='national_inv')
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)

visualize_boxplot()
st.subheader('Issue BackOrder')
@st.cache_data
def visualize_piechart():
    tab1, tab2 = st.tabs(['Potential Issue', 'Stop auto buy'])
    with tab1:
        pie_data = df.groupby(['went_on_backorder', 'potential_issue']).size().reset_index(name='counts')
        fig = px.pie(pie_data, names='potential_issue', values='counts', title='Pie Chart of Potential Issue by Backorder')
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)
    with tab2:
        pie_data = df.groupby(['went_on_backorder', 'stop_auto_buy']).size().reset_index(name='counts')
        fig = px.pie(pie_data, names='stop_auto_buy', values='counts', title='Pie Chart of Stop Auto Buy by Backorder')
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)

visualize_piechart()