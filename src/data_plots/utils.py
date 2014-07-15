def labeler(axes, **kwargs):
    xlabel = kwargs.get('xlabel')
    ylabel = kwargs.get('ylabel')
    zlabel = kwargs.get('zlabel')
    if xlabel:
        axes.set_xlabel(xlabel)
    if ylabel:
        axes.set_ylabel(ylabel)
    if zlabel:
        axes.set_zlabel(zlabel)

    return axes

def titler(axes, **kwargs):
    title = kwargs.get('title')
    if title:
        axes.set_title(title)

    return axes
