import streamlit as st
import pandas as pd
import os

# DATA LOADING FUNCTIONS
#--------------------------------------------------------
@st.cache
def load_data(filename=None):
    if not filename:
        folder = 'streamlt-matplotlib/items'
        filename = 'sample_data.csv'
        path = os.path.join(folder, filename)
        data = pd.read_csv(path)
    else:
        data = pd.read_csv(filename)
    return data

@st.cache
def get_data_columns(data):
    return list(data.columns)
#--------------------------------------------------------

def get_weight(bold):
    if bold:
        return 'bold'
    else:
        return 'normal'
 