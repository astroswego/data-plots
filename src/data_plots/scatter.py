import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def scatter3d(x, y, z, elev=0, azim=0, *args, **kwargs):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z)
    ax.elev, ax.azim = elev, azim

    return fig

def scatter3d_from_file(input, *args, usecols=range(3), **kwargs):
    x, y, z = numpy.loadtxt(input, usecols=usecols, unpack=True)

    return scatter3d(x, y, z, *args, **kwargs)
