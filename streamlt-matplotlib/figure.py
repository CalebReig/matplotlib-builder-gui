import matplotlib.pyplot as plt
from utils import get_weight



class Figure():

    def __init__(self, width=10, height=5, rows=1, columns=1):
        plt.rcParams["figure.figsize"] = (width,height)
        self.fig, self.axs = plt.subplots(rows, columns)
        self.rows = rows
        self.columns = columns
        self.num_plots = rows * columns

    def set_background_color(self, color='#f5f5f5'):
        self.fig.patch.set_facecolor(color)

    def hist_plot(self, ax_ix1, data, ax_ix2=None, chart_options={}):
        ax = self.axs
        if self.rows > 1 and  self.columns > 1:
            ax = self.axs[ax_ix1, ax_ix2]
        elif self.num_plots > 1:
            ix = ax_ix1
            if ax_ix2 > ax_ix1:
                ix = ax_ix2
            ax = self.axs[ix]
        ax.hist(data[chart_options['col']], bins=chart_options['bins'],
                color=chart_options['color'])
        ax.set_title(chart_options['title'], {'size': chart_options['title_size'], 
                    'weight': get_weight(chart_options['title_weight'])})
        ax.set_xlabel(chart_options['xlabel'], {'size': chart_options['xlabel_size'],
                    'weight': get_weight(chart_options['xlabel_weight'])})
        ax.set_ylabel(chart_options['ylabel'], {'size': chart_options['ylabel_size'],
                    'weight': get_weight(chart_options['ylabel_weight'])})

    def box_plot(self, ax_ix1, data, ax_ix2=None, chart_options={}):
        ax = self.axs
        if self.rows > 1 and  self.columns > 1:
            ax = self.axs[ax_ix1, ax_ix2]
        elif self.num_plots > 1:
            ix = ax_ix1
            if ax_ix2 > ax_ix1:
                ix = ax_ix2
            ax = self.axs[ix]
        ax.boxplot(data[chart_options['col']], showfliers=chart_options['outliers'], 
                        vert=chart_options['vert'])
        ax.set_title(chart_options['title'], {'size': chart_options['title_size'], 
                    'weight': get_weight(chart_options['title_weight'])})
        ax.set_xlabel(chart_options['xlabel'], {'size': chart_options['xlabel_size'],
                    'weight': get_weight(chart_options['xlabel_weight'])})
        ax.set_ylabel(chart_options['ylabel'], {'size': chart_options['ylabel_size'],
                    'weight': get_weight(chart_options['ylabel_weight'])})