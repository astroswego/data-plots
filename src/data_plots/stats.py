import numpy
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
from matplotlib import rcParams
from scipy.optimize import curve_fit

from data_plots.utils import labeler, titler

rcParams['text.usetex'] = True

def scatter_hist(x, y, *args,
        bins=10,
        linestyle='r--', scatterstyle='k+',
        histtype='stepfilled', facecolor='#FFFFFF', hatch='/',
        show_mean=True, show_std=True,
        **kwargs):
    # no labels
    nullfmt = NullFormatter()

    # definitions for axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left+width+0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    # start with a rectangular Figure
    fig = plt.figure(1, figsize=(8, 8))

    axScatter = fig.add_axes(rect_scatter)
    axHistx = fig.add_axes(rect_histx)
    axHisty = fig.add_axes(rect_histy)

    # no labels on some axes
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # the scatter plot:
    axScatter.plot(x, y, scatterstyle)

    # determine limits
    xmin, ymin = numpy.min(x), numpy.min(y)
    xmax, ymax = numpy.max(x), numpy.max(y)
    x_mean, y_mean = x.mean(), y.mean()
    x_std,  y_std  = x.std(),  y.std()
#    xlims = ((numpy.array([-xmin, xmax]) // binwidth) + 1) * binwidth
#    ylims = ((numpy.array([-ymin, ymax]) // binwidth) + 1) * binwidth
    xbins = numpy.linspace(xmin, xmax, bins)
    ybins = numpy.linspace(ymin, ymax, bins)

#    xbins = numpy.arange(-xlims[0], xlims[1]+binwidth, binwidth)
#    ybins = numpy.arange(-ylims[0], ylims[1]+binwidth, binwidth)
    n, xbins, xpatches = axHistx.hist(x, bins=xbins, normed=1,
                                      histtype=histtype, facecolor=facecolor,
                                      hatch=hatch)
    n, ybins, ypatches = axHisty.hist(y, bins=ybins, normed=1,
                                      histtype=histtype, facecolor=facecolor,
                                      hatch=hatch,
                                      orientation='horizontal')
    

    
    mean_formatter = r'$\mu = {0:.5f}$'.format
    std_formatter = r'$\sigma = {0:.5f}$'.format
    xhandles, yhandles = [], []
    xlabels, ylabels = [], []
    if show_mean:
        p = plt.Rectangle((0, 0), 1, 1, fc="r")
        xlabels.append(mean_formatter(x_mean))
        ylabels.append(mean_formatter(y_mean))
        xhandles.append(p)
        yhandles.append(p)
    if show_std:
        p = plt.Rectangle((0, 0), 1, 1, fc="b")
        xlabels.append(std_formatter(x_std))
        ylabels.append(std_formatter(y_std))
        xhandles.append(p)
        yhandles.append(p)

    if show_mean or show_std:
        axHistx.legend(xhandles, xlabels,
                       fontsize='small', loc='upper right')
        axHisty.legend(xhandles, xlabels,
                       fontsize='small', loc='upper right')

    
        
    xpdf = mlab.normpdf(xbins, x_mean, x_std)
    ypdf = mlab.normpdf(ybins, y_mean, y_std)

    axHistx.plot(xbins, xpdf, linestyle)
    axHisty.plot(ypdf, ybins, linestyle)

    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())

    axHistx.locator_params(tight=False, nbins=3)
    axHisty.locator_params(tight=False, nbins=3)

    axHistx = titler(axHistx, **kwargs)
    axScatter = labeler(axScatter, **kwargs)

    return fig

def scatter_hist_from_file(input, *args, usecols=range(2), **kwargs):
    x, y = numpy.loadtxt(input, usecols=usecols, unpack=True)
    return scatter_hist(x, y, *args, **kwargs)

def _gauss(x, *p):
    A, mu, sigma = p
    return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))
