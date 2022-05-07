import streamlit as st


def expand_annotation(options, annot):
    supported_annots = {
        'Text': annot_text,
        'Arrow': annot_arrow
    }
    supported_annots[options['type']](options, annot)


def annot_text(options, annot):
    options['text'] = st.text_input('Text', key=str(annot)+'_text')
    options['size'] = st.slider('Size', 0, 72, 14, key=str(annot)+'_size')
    options['x'] = st.slider('X Position', -50, 150, 0, 1, key=str(annot)+'_x')
    options['y'] = st.slider('Y Position', -50, 150, 0, 1, key=str(annot)+'_y')


def annot_arrow(options, annot):
    options['x'] = st.slider('X Position (Start)', -5, 80, 0, 1, key=str(annot)+'_x')
    options['y'] = st.slider('Y Position (Start)', -5, 80, 0, 1, key=str(annot)+'_y')
    options['x2'] = st.slider('X Position (End)', -5, 80, 0, 1, key=str(annot)+'_x2')
    options['y2'] = st.slider('Y Position (End)', -5, 80, 0, 1, key=str(annot)+'_y2')



def annotate(figure, options):
    supported_annots = {
        'Text': figure.text,
        'Arrow': figure.arrow
    }
    supported_annots[options['type']](options)