import streamlit as st
from utils import *

def expand_chart(options, data, sub_ax):
    supported_charts = {
        'Histogram': histogram_expander,
        'Box Plot': boxplot_expander
    }
    supported_charts[options['type']](options, data, sub_ax)

def boxplot_expander(options, data, sub_ax):
        options['col'] = st.selectbox('Column', get_data_columns(data), 
                key=str(sub_ax)+'_box_col')
        options['outliers'] = st.checkbox('Show Outliers', True, key=str(sub_ax)+'show_outlier')
        options['vert'] = st.checkbox('Vertical', key=str(sub_ax)+'vertical') 
    
          
        

def histogram_expander(options, data, sub_ax):
        options['col'] = st.selectbox('Column', get_data_columns(data), 
                key=str(sub_ax)+'_hist_col')
        options['color'] = st.color_picker('Color', '#808080', key=str(sub_ax)+'hist_color')
        options['bins'] = st.slider('Bins', 1, 100, 10, key=str(sub_ax)+'bins')


def plot(figure, ax_ix1, ax_ix2, data, chart_options):
    supported_plots = {
        'Histogram': figure.hist_plot,
        'Box Plot': figure.box_plot
    }
    supported_plots[chart_options['type']](ax_ix1=ax_ix1, ax_ix2=ax_ix2, 
                    data=data, chart_options=chart_options)
