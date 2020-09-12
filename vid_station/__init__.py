import sys
import datetime

from .options import parse_options
from .utils import add_extension, process_batch
from .RapidClip import RapidClip


def _real_main(argv=None):
    # Get command options
    opts = parse_options(argv)
    options = {'opts': opts, 'source': argv[1]}

    # If this is a batch file, run process video on each filename.
    if opts.batch is not None:
        process_batch(opts)
    else:
        RapidClip(options).process()



def main(argv=None):
    try:
        _real_main(argv)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
