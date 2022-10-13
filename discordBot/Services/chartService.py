import matplotlib.pyplot as plt
import io

class ChartService():

    def killChart(self, username, kills):
        f, ax = plt.subplots()

        ax.bar(username, kills)

        ax.set_ylabel('Kills')

        fig = plt.gcf()

        return self.fig2img(fig)

    def fig2img(self, fig):
        buf = io.BytesIO()
        fig.savefig(buf)
        buf.seek(0)
        return buf