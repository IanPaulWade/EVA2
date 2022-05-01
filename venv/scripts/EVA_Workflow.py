
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import io
import os
import corner
from numpy import ndarray

from scipy import stats

path = "/Users/ian/Documents/PycharmProjects/EVA/venv/data/"
filename = "SEASTATES_Loc01.mat"

mat_data = sio.loadmat(os.path.join(path,filename))
#print(mat_data)

Hs = mat_data['Hs']
Tp = mat_data['Tp']
Tz = mat_data['Tz']
WS = mat_data['Wnd_Spd10']

Hs = np.array(Hs)
Tp = np.array(Tp)
Tz = np.array(Tz)
WS = np.array(WS)
noVars = 3

nsamples = len(Hs)
samples = np.hstack([Hs,Tp,WS]).reshape([nsamples,noVars])

figure = corner.corner(samples, bins = 20, quantiles = [0.05,0.50,0.95], show_titles = True,
    labels=[r"Hs (m)", r"Tp (s)",r"WS (m/s)"], title_kwargs={"fontsize": 12},
    color = "grey", figsize = (16,16), plot_contours = True,
    fill_contours = True)

modeData = stats.mode(samples, axis = 0)
modeData2 = modeData.mode

# Extract the axes
axes = np.array(figure.axes).reshape((noVars, noVars))

# Loop over the diagonal
for i in range(noVars):
    ax = axes[i, i]
    ax.axvline(modeData2[:,i], color="C1",lw = 0.5)

    ax.axvline(np.quantile(samples[:,i], .99), color="C2",lw = 0.5)
    ax.axvline(np.quantile(samples[:,i], .999), color="C3",lw = 0.5)
    ax.axvline(np.quantile(samples[:,i], .9999), color="C4",lw = 0.5)

# Loop over the histograms
for yi in range(noVars):
    for xi in range(yi):
        ax = axes[yi, xi]

        ax.axvline(modeData2[:,xi], color="C1", lw = 0.5)
        ax.axhline(modeData2[:,yi], color="C1", lw = 0.5)
        ax.plot(modeData2[:,xi], modeData2[:,yi], "sC1", lw = 0.5)

        ax.axvline(np.quantile(samples[:,xi], .99), color="C2", lw = 0.5)
        ax.axhline(np.quantile(samples[:,yi], .99), color="C2", lw = 0.5)
        ax.plot(np.quantile(samples[:,xi], .99), np.quantile(samples[:,yi], .99), "sC2", lw = 0.5)

        ax.axvline(np.quantile(samples[:, xi], .999), color="C3", lw=0.5)
        ax.axhline(np.quantile(samples[:, yi], .999), color="C3", lw=0.5)
        ax.plot(np.quantile(samples[:, xi], .999), np.quantile(samples[:, yi], .999), "sC3", lw=0.5)

        ax.axvline(np.quantile(samples[:, xi], .9999), color="C4", lw=0.5)
        ax.axhline(np.quantile(samples[:, yi], .9999), color="C4", lw=0.5)
        ax.plot(np.quantile(samples[:, xi], .9999), np.quantile(samples[:, yi], .9999), "sC4", lw=0.5)

#plt.show()
figure.savefig("corner.tif", dpi = 400)
# test test test test

# TEST NEW BRANCH 2 new remote repo test EVA to EVA2
# github edit

# xlim = [0,30] #Tp.min(), Tp.max()
# ylim = [0,10] #Hs.min(), Hs.max()
#
# fig, (ax1) = plt.subplots(ncols = 1, sharey = False, figsize = (12,12))
#
# hb = ax1.hexbin(Tp, Hs, gridsize = 200, bins = 'log', cmap = 'jet')
#
# ax1.set(xlim = xlim, ylim = ylim)
# ax1.set_title("With a log color scale")
# ax1.set_xlabel("Tp (s)")
# ax1.set_ylabel("Hs (m)")
#
# cb = fig.colorbar(hb, ax = ax1, label = 'log10(N)')
#
# plt.show()
