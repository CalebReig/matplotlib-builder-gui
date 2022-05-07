from utils import *

def find_plot_ix(subplot, chain_options):
    rows_over_1 = False
    cols_over_1 = False
    for sub in chain_options:
        if sub[0] > 0:
            rows_over_1 = True
        if sub[1] > 0:
            cols_over_1 = True
        if rows_over_1 and cols_over_1:
            break
    ix = str(subplot[0])
    if rows_over_1 and cols_over_1:
        ix = "{}, {}".format(subplot[0], subplot[1])
    elif cols_over_1:
        ix = str(subplot[1])
    return ix

#PLOTS
# ---------------------------------------------
def make_plot_code(chart_options, ix):
    supported_plots = {
        'Histogram': hist_plot_code,
        'Box Plot': box_plot_code
    }
    return supported_plots[chart_options['type']](chart_options, ix)

def hist_plot_code(chart_options, ix):
    code = \
    """axs[{ix}].{plot_type}(x=data['{col}'], bins={bins}, color='{color}')
    """.format(ix=ix, plot_type='hist',  
                col=chart_options['col'], bins=chart_options['bins'],
                color=chart_options['color'])
    return code

def box_plot_code(chart_options, ix):
    code = \
    """axs[{ix}].{plot_type}(x=data['{col}'], showfliers={outliers}, vert='{vert}')
    """.format(ix=ix, plot_type='boxplot',  
                col=chart_options['col'], outliers=chart_options['outliers'],
                vert=chart_options['vert'])
    return code

# CONCAT ALL PLOT CODE TOGETHER
def make_subplot_code(chart_options):
    code = ""
    for subplot in chart_options:
        ix=find_plot_ix(subplot, chart_options)
        op = chart_options[subplot]
        sub_code = \
            """
    #SUBPLOT {subplot}
    {plot_type}
    axs[{ix}].set_title('{title}', {{'size': '{title_size}', 'weight': '{title_weight}'}})
    axs[{ix}].set_xlabel('{xlabel}', {{'size': '{xlabel_size}', 'weight': '{xlabel_weight}'}})
    axs[{ix}].set_ylabel('{ylabel}', {{'size': '{ylabel_size}', 'weight': '{ylabel_weight}'}})
    """.format(subplot=subplot, ix=ix, 
                        plot_type=make_plot_code(chart_options[subplot], ix),
                        title=op['title'], title_size=op['title_size'],
                        title_weight=get_weight(op['title_weight']), xlabel=op['xlabel'], 
                        xlabel_size=op['xlabel_size'], xlabel_weight=get_weight(op['xlabel_weight']),
                        ylabel=op['ylabel'], ylabel_size=op['ylabel_size'],
                        ylabel_weight=get_weight(op['ylabel_weight']))
            
        code += sub_code
    return code


# ANNOTATIONS
# -----------------------------------------------------
def make_annotation_code(annotation_options):
    supported_annotations = {
        'Text': annot_text_code,
        'Arrow': annot_arrow_code
    }
    return supported_annotations[annotation_options['type']](annotation_options)

def annot_text_code(op):
    code = \
        """fig.text({x}, {y}, '{text}', {{'size': '{size}'}})""".format(
            x=op['x'], y=op['y'], text=op['text'], size=op['size']
        )
    return code

def annot_arrow_code(op):
    code = \
       """plt.annotate('', xy=({x1}, {y1}), xycoords='figure points', 
                xytext=({x2}, {y2}), arrowprops=dict(arrowstyle='->', lw=5))""".format(
                        x1=op['x'], y1=op['y'], x2=op['x2'], y2=op['y2']
                    )
    return code


# COMBINE ALL ANNOTATIONS
def make_all_annotations(annotation_options):
    code = "" 
    added_comment = False
    for annot in annotation_options:
        if not added_comment:
            code += """#SET ANNOTATION OPTIONS
    """
        code += make_annotation_code(annotation_options[annot])
    return code
        

#ALL CODE TOGETHER

def make_fig_code(figure_options, chart_options, annotation_options):
    code = \
    """
    ```python 
    #IMPORT LIBRARIES
    import matplotlib.pyplot as plt
    import pandas as pd

    #READ IN DATA
    data = pd.read_csv('{filename}')
    
    #SET FIGURE OPTIONS
    plt.rcParams["figure.figsize"] = ({width}, {height})
    fig, axs = plt.subplots({rows}, {columns})
    fig.patch.set_facecolor('{background_color}')

    #SET SUBPLOT OPTIONS
    #-------------------------------- {subplot_info}
    {annotation_info}

    plt.show()
    ```
    """.format(filename=figure_options['data'], width=figure_options['width'],
                 height=figure_options['height'], rows=figure_options['rows'], 
                 columns=figure_options['columns'], 
                 background_color=figure_options['background_color'], 
                 subplot_info=make_subplot_code(chart_options),
                 annotation_info=make_all_annotations(annotation_options))
    return code
