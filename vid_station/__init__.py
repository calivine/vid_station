import sys
import datetime

from .options import parse_options
from .RapidClip import RapidClip


def _real_main(argv=None):
    # Get command options
    opts = parse_options(argv)
    options = {'opts': parse_options(argv), 'source': argv[1]}

    # If this is a batch file, run process video on each filename.
    if options['opts'].batch is not None:
        RapidClip(options).process_batch()
    else:
        RapidClip(options).process()


def main(argv=None):
    try:
        _real_main(argv)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
