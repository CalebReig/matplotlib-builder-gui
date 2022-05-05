import streamlit as st
from utils import *

def expand_text(options, sub_ax):
    
    options['title'] = st.text_input("Title", key=str(sub_ax)+'title')
    options['title_weight'] = st.checkbox('Bold', False, key=str(sub_ax)+'title_weight')
    options['title_size'] = st.slider("Title: Text Size", 0, 72, 20, 1,
                    key=str(sub_ax)+'title_size')
    options['xlabel'] = st.text_input("X-Axis Label", key=str(sub_ax)+'xlabel')
    options['xlabel_weight'] = st.checkbox('Bold', False, key=str(sub_ax)+'xlabel_weight')
    options['xlabel_size'] = st.slider("X Axis: Text Size", 0, 72, 20, 1, 
                    key=str(sub_ax)+'xlabel_size')
    options['ylabel'] = st.text_input("Y-Axis Label", key=str(sub_ax)+'ylabel')
    options['ylabel_weight'] = st.checkbox('Bold', False, key=str(sub_ax)+'ylabel_weight')
    options['ylabel_size'] = st.slider("Y-Axis: Text Size", 0, 72, 20, 1, 
                    key=str(sub_ax)+'ylabel_size')