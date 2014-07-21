import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from matplotlib.mlab import griddata

def contour(x, y, z, dx, dy, *args, cmap='Reds', interp='linear', **kwargs):
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    z_min, z_max = z.min(), z.max()

#    ygrid, xgrid = numpy.mgrid[y_min : y_max+dy : dy,
#                               x_min : x_max+dx : dx]
#    xgrid, ygrid = numpy.meshgrid(x, y)
    xi = numpy.arange(x_min, x_max+dx, dx)
    yi = numpy.arange(y_min, y_max+dy, dy)
    zi = griddata(x, y, z, xi, yi, interp=interp)
#    z = z.reshape(xgrid.shape)
    levels = MaxNLocator(nbins=15).tick_values(z_min, z_max)

    cmap_ = plt.get_cmap(cmap)
    norm = BoundaryNorm(levels, ncolors=cmap_.N, clip=True)

    fig, ax = plt.subplots(1, 1)
    im = ax.pcolormesh(xi, yi, zi, cmap=cmap_, norm=norm)
    fig.colorbar(im)
    ax.axis([x_min, x_max, y_min, y_max])

    return fig

def contour(*args, **kwargs):
    fig, ax = plt.subplots(1, 1)

    return plot_contour(fig, ax, *args, **kwargs)[0]

def plot_contour(fig, ax, x, y, z, dx, dy, *args, cmap='Reds', interp='linear',
                 **kwargs):
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    z_min, z_max = z.min(), z.max()

#    ygrid, xgrid = numpy.mgrid[y_min : y_max+dy : dy,
#                               x_min : x_max+dx : dx]
#    xgrid, ygrid = numpy.meshgrid(x, y)
    xi = numpy.arange(x_min, x_max+dx, dx)
    yi = numpy.arange(y_min, y_max+dy, dy)
    zi = griddata(x, y, z, xi, yi, interp=interp)
#    z = z.reshape(xgrid.shape)
    levels = MaxNLocator(nbins=15).tick_values(z_min, z_max)

    cmap_ = plt.get_cmap(cmap)
    norm = BoundaryNorm(levels, ncolors=cmap_.N, clip=True)

    im = ax.pcolormesh(xi, yi, zi, cmap=cmap_, norm=norm)
    fig.colorbar(im)
    ax.axis([x_min, x_max, y_min, y_max])

    return fig, ax

def contour_from_file(input, *args, usecols=range(3), **kwargs):
    x, y, z = numpy.loadtxt(input, usecols=usecols, unpack=True)

    return contour(x, y, z, *args, **kwargs)
