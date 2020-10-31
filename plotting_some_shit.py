import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import AutoMinorLocator
import numpy as np

# График линейной зависимости по канонам ВТЭК
def vtek_linear_ploting(xmin, xmax, ymin, ymax, 
                        title, xlabel, ylabel, 
                        xdata, ydata, xerr = None, yerr = None, 
                        imagename='imagename'):
    """
    xmin, xmax, ymin, ymax: Диапозоны графика
    title, xlabel, ylabel: Заголовок и подписи осей
    xdata, ydata: Экспериментальные точки
    linedata: Данные линейной аппроксимации
    imagename: Название сохраняемой картинки
    xyerr, yerr: Погрешности по x и y (по умолчаню отсутствуют)
    """

    fig = plt.figure(figsize=[6.5,4.25], dpi=100)
    ax = fig.gca()

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    
    ax.set_xscale("linear")
    ax.set_yscale("linear")
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(direction="in", length=4, width=1.25)
    ax.tick_params(which="minor", direction="in")
    ax.grid(c='grey', ls='--', lw=1)
    ax.spines["bottom"].set_linewidth(1.5)
    ax.spines["right"].set_linewidth(1.5)
    ax.spines["left"].set_linewidth(1.5)
    ax.spines["top"].set_linewidth(1.5)

    ax.set_title(title,
                fontproperties=FontProperties(family='ubuntu', style='normal', weight='heavy', size=13), 
                pad=15)
    ax.set_xlabel(xlabel, fontdict={'fontsize': 10}, labelpad=0)
    ax.set_ylabel(ylabel, fontdict={'fontsize': 10}, labelpad=5)
    ax.errorbar(xdata, ydata, xerr=xerr, yerr=yerr, fmt='ks', capsize=3, ms=6, label='Эксперимент')
    
    lstsq = np.linalg.lstsq(np.dstack((xdata, np.ones(len(xdata))))[0], ydata)[0].tolist()
    a = lstsq[0]
    b = lstsq[1]
    linedata = np.array(xdata)*a + b
    print(f'МНК: y={a}*x + {b}')
    label_string = rf'МНК: $y={np.round(a, 3)}*x+({np.round(b, 3)})$'
    ax.plot(xdata, linedata, '-b', lw=2.5, label=label_string)
    
    ax.legend(loc='upper left')

    fig.savefig(imagename, dpi=300, bbox_inches = "tight")
    fig.show()
    