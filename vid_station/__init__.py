import os
import sys


from .options import parseOpts
from .app import ProcessVideo
from .util import add_extension


def _real_main(argv=None):
    opts = parseOpts(argv)
    if opts.batch is not None:
        f = open(opts.batch, 'r')
        i = 0
        while True:
            line = f.readline()
            if not line:
                break
            filename = add_extension(line[:-1])
            print(str(i), filename)
            ProcessVideo(filename, opts)
            i += 1
        f.close()
    else:
        ProcessVideo(add_extension(argv[1]), opts)


def main(argv=None):
    try:
        _real_main(argv)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
