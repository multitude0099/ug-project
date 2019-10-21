import warnings

import pandas as pd
from matplotlib import animation
from matplotlib import pyplot as plt

from dataset import suny_international

plt.rcParams["figure.figsize"] = (20, 3)
warnings.filterwarnings("ignore")


def plot_daily(*dfs, save=None):
    fig = plt.figure()
    max_y = max((df.max() for df in dfs))
    xlim = (dfs[0].index.time.min(), dfs[0].index.time.max())
    ax = plt.axes(ylim=(0, max_y), xlim=xlim)
    lines = [ax.plot([], [], 'o-', lw=2)[0] for _ in dfs]
    df_days = [df.groupby(pd.Grouper(freq='D')) for df in dfs]
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def init():
        for line in lines:
            line.set_data([], [])
        time_text.set_text('')
        return lines + [time_text]

    def update(df):
        for df_day, line in zip(df, lines):
            line.set_data(df_day[1].index.time, list(df_day[1]))
        time_text.set_text(df[0][0].strftime("%b %Y"))
        return lines + [time_text]

    anim = animation.FuncAnimation(fig, update, frames=zip(*df_days), init_func=init, blit=True, interval=20)
    if save:
        anim.save(save)
    plt.show()


if __name__ == "__main__":
    plot_daily(suny_international()['ghi'], save='plot_simple.mp4')
