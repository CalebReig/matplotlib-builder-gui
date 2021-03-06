import streamlit as st
from utils import *
from code_generator import *
from chart_expander import *
from text_expander import *
from annotation_expander import *
from figure import Figure
import io


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

try:
    if st.session_state['upload_data']: 
        figure_options['data'] = st.session_state['upload_data'].name
    else:
        figure_options['data'] = 'sample_data.csv'
except:
    figure_options['data'] = 'sample_data.csv'


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
for sub_ax in figure.list_subaxs():
    chart_options[sub_ax] = {}
    with st.sidebar.expander("SUBPLOT: " + str(sub_ax), expanded=False):
        st.write('#### Chart Options')
        chart_options[sub_ax]['type'] = st.selectbox('Chart Type', ['Histogram', 'Box Plot'], key=str(sub_ax) + '_type')
        chart_placeholder = st.empty()
        with chart_placeholder.container():
            expand_chart(chart_options[sub_ax], data, sub_ax)
        st.write('#### Text Options')
        expand_text(chart_options[sub_ax], sub_ax)

        plot(figure=figure, ax_ix1=sub_ax[0], ax_ix2=sub_ax[1], 
                        data=data, chart_options=chart_options[sub_ax])


# ANNOTATIONS
annotation_options = {}
st.sidebar.markdown("## Annotation Options")
num_annots = st.sidebar.number_input("Number of Annotations", 0, 10, 0)

for annot in range(int(num_annots)):
    annotation_options[annot] = {}
    with st.sidebar.expander("ANNOTATION " + str(annot), expanded=False):
        annotation_options[annot]['type'] = st.selectbox('Type', ['Text', 'Arrow'], 
                                                        key=str(annot) + '_type')
        annot_placeholder = st.empty()
        with annot_placeholder.container():
            expand_annotation(annotation_options[annot], annot)
        annotate(figure=figure, options=annotation_options[annot])

#--------------------------------------------------------


st.markdown("### Figure Preview")
st.pyplot(figure.fig)

#TROUBLE SHOOTING THE BELOW CODE
buf = io.BytesIO()
figure.fig.savefig(buf, format='png')
buf.seek(0)
st.download_button('Download', buf, file_name='graph.png')

with st.expander("CODE"):
    st.markdown(make_fig_code(figure_options, chart_options, annotation_options))

st.session_state['upload_data'] = st.file_uploader("Upload Your CSV File")
st.markdown("### Data Sample")
st.write(data.head())
