import sys
import datetime

from .options import parse_options
from .app import process_video


def add_extension(source, ext=".mp4"):
    if source.endswith(".mp4"):
        return source
    else:
        return source + ext


def _real_main(argv=None):
    # Get command options
    opts = parse_options(argv)

    # If this is a batch file, run process video on each filename.
    if opts.batch is not None:
        f = open(opts.batch, 'r')
        i = 0
        while True:
            line = f.readline()
            if not line:
                break
            filename = add_extension(line[:-1])
            print(str(i), filename)
            process_video(filename, opts)
            i += 1
        f.close()
    else:
        process_video(add_extension(argv[1]), opts)


def main(argv=None):
    try:
        _real_main(argv)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
