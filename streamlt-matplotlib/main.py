import streamlit as st
from utils import *
from figure import Figure


try:
    data = load_data(st.session_state['upload_data'])
except:
    data = load_data()



st.title('Matplotlib Graph Builder GUI')

# SIDEBAR OPTIONS
#--------------------------------------------------------
#FIGURE
st.sidebar.markdown("## Figure Options")
figure_options = {}
with st.sidebar.expander("FIGURE OPTIONS", expanded=False):
    figure_options['height'] = int(st.number_input("Height", 3, 30, 5))
    figure_options['width'] = int(st.number_input("Width", 3, 30, 10))
    figure_options['rows'] = int(st.number_input("Rows", 1))
    figure_options['columns'] = int(st.number_input("Columns", 1))
    figure_options['background_color'] = st.color_picker('Background Color', '#f5f5f5')

# CREATE FIGURE OBJECT
figure = Figure(height=figure_options['height'], width=figure_options['width'],
                                     rows=figure_options['rows'], columns=figure_options['columns'])
figure.set_background_color(figure_options['background_color'])

#SUBPLOTS
st.sidebar.markdown("## Subplot Options")
chart_options = {}
for sub_ax in [(i, j) for i in range(figure_options['rows']) for j in range(figure_options['columns'])]:
    chart_options[sub_ax] = {}
    with st.sidebar.expander("SUBPLOT: " + str(sub_ax), expanded=False):
        chart_options[sub_ax]['col'] = st.selectbox('Column', get_data_columns(data), key=str(sub_ax)+'_col')
        chart_options[sub_ax]['type'] = st.selectbox('Chart Type', ['Histogram'], key=str(sub_ax) + '_type')
        chart_options[sub_ax]['color'] = st.color_picker('Color', '#808080', key=str(sub_ax)+'_color')
        chart_options[sub_ax]['title'] = st.text_input("Title", key=str(sub_ax)+'_title')
        chart_options[sub_ax]['title_weight'] = st.checkbox('Bold', False,key=str(sub_ax)+'_titleweight')
        chart_options[sub_ax]['title_size'] = st.slider("Title: Text Size", 0, 72, 20, 1, 
                                                        key=str(sub_ax)+'_titletext')
        chart_options[sub_ax]['xlabel'] = st.text_input("X-Axis Label", key=str(sub_ax)+'_xlabel')
        chart_options[sub_ax]['xlabel_weight'] = st.checkbox('Bold', False, key=str(sub_ax)+'_xlabelweight')
        chart_options[sub_ax]['xlabel_size'] = st.slider("X Axis: Text Size", 0, 72, 20, 1, 
                                                        key=str(sub_ax)+'_xlabeltext')
        chart_options[sub_ax]['ylabel'] = st.text_input("Y-Axis Label", key=str(sub_ax)+'_ylabel')
        chart_options[sub_ax]['ylabel_weight'] = st.checkbox('Bold', False, key=str(sub_ax)+'_ylabelweight')
        chart_options[sub_ax]['ylabel_size'] = st.slider("Y-Axis: Text Size", 0, 72, 20, 1, 
                                                        key=str(sub_ax)+'_ylabeltext')
        plot(figure=figure, ax_ix1=sub_ax[0], ax_ix2=sub_ax[1], 
                        data=data, chart_options=chart_options[sub_ax])




#--------------------------------------------------------


st.markdown("### Figure Preview")
st.pyplot(figure.fig)
figure.fig.savefig('graph.png')

st.download_button('Download', open('graph.png', 'rb'), file_name='graph.png')
with st.expander("CODE"):
    st.markdown(make_fig_code(figure_options, chart_options))

st.session_state['upload_data'] = st.file_uploader("Upload Your CSV File")
st.markdown("### Data Sample")
st.write(data.head())
