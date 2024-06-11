import streamlit as st

st.set_page_config(
    page_title="Main page",
)

st.markdown("# Back Order Modeling")#judul, ##subjdul,###subjudul lebihkecil

st.markdown(
    """
    Welcome to Home Page!

    **👈 Select any pages from the sidebar** to see Data, Analysis and Model.

    ### Objective
    - Analysing data
    - Make model to detect product need **Back Order** or no
        
    ### Model
    - Random Forest
    - XGBoost
"""
)