from argparse import ArgumentParser, ArgumentError, SUPPRESS
from os import path
from data_plots.scatter import scatter3d_from_file
from data_plots.stats import scatter_hist_from_file




def get_args():
    single_output_parser = ArgumentParser(add_help=False)
    single_output_parser.add_argument('--filename',
        type=str,
        help='Name of file to save (does not include extension)')
    threedee_parser = ArgumentParser(add_help=False)
    threedee_parser.add_argument('--azimuth', dest='azim',
        type=float, default=0.0,
        help='Azimuth angle for 3D plot.')
    threedee_parser.add_argument('--elevation', dest='elev',
        type=float, default=0.0,
        help='Elevation angle for 3D plot.')

    parser = ArgumentParser(prog='data-plots')
    label_parser = parser.add_argument_group('Labels')

    parser.add_argument('-i', '--input',
        help='Input file.')
    parser.add_argument('-o', '--output',
        help='Output directory.')
    parser.add_argument('-c', '--usecols',
        type=int, nargs='+', default=SUPPRESS, metavar='C',
        help='Columns in input file to use')
    parser.add_argument('-t', '--type',
        type=str, default='.png',
        help='File type to output')
    parser.add_argument('--show-only',
        default=False, action='store_true',
        help='Show figure instead of saving')

    label_parser.add_argument('--title',
        type=str, default=SUPPRESS,
        help='Figure title')
    label_parser.add_argument('--xlabel',
        type=str, default=SUPPRESS,
        help='Figure x label')
    label_parser.add_argument('--ylabel',
        type=str, default=SUPPRESS,
        help='Figure y label')
    label_parser.add_argument('--zlabel',
        type=str, default=SUPPRESS,
        help='Figure z label')

    plot_parser = parser.add_subparsers(title='plot type')

    scatter_hist_parser = plot_parser.add_parser('scatter_hist',
        parents=[single_output_parser])
    scatter_hist_parser.add_argument('--bin-size',
        type=float, default=SUPPRESS, metavar='SIZE',
        help='Histogram bin size')
    scatter_hist_parser.add_argument('--show-mean',
        default=SUPPRESS, action='store_true',
        help='Show mean on histograms.')
    scatter_hist_parser.add_argument('--show-std',
        default=SUPPRESS, action='store_true',
        help='Show standard deviation on histograms.')
    scatter_hist_parser.set_defaults(plot=scatter_hist_from_file,
                                     filename='scatter_hist')

    scatter3d_parser = plot_parser.add_parser('scatter3d',
        parents=[single_output_parser, threedee_parser])
    scatter3d_parser.set_defaults(plot=scatter3d_from_file,
                                  filename='scatter3d')

    return parser.parse_args()

def main():
    args = get_args()

    fig = args.plot(**vars(args))
    if args.show_only:
        fig.show()
    else:
        fig.savefig(path.join(args.output, args.filename))
    fig.clf()
