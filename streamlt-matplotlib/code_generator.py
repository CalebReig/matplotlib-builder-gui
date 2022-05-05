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





    return code

def make_fig_code(figure_options={}, chart_options={}):
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
    #--------------------------------
    {subplot_info}
    plt.show()
    ```
    """.format(filename=figure_options['data'], width=figure_options['width'],
                 height=figure_options['height'], rows=figure_options['rows'], 
                 columns=figure_options['columns'], 
                 background_color=figure_options['background_color'], 
                 subplot_info=make_subplot_code(chart_options))
    return code
