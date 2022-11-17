from typing import List
import matplotlib.pyplot as plt
import matplotlib as mpl
import io

class ChartService():

    def killChart(self, username: List[str], kills, colors: List[str]):
        mpl.rcParams['axes.labelcolor'] = 'White'
        mpl.rcParams['text.color'] = 'White'
        mpl.rcParams['xtick.color'] = 'White'
        mpl.rcParams['ytick.color'] = 'White'
        mpl.rcParams['font.size'] = '12'
        f, ax = plt.subplots()
        #Not using colors rn
        ax.bar(username, kills, color='orange')

        ax.set_ylabel('Kills')
    
        ax.set_title('Y7S3: BRUTAL SWARM KILLS')

        ax.set_facecolor('#36393e')

        f.set_facecolor('#36393e')

        fig = plt.gcf()

        return self.fig2img(fig)

    def fig2img(self, fig):
        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        return buf