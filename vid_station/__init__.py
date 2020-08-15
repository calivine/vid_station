import os
import sys


from .options import parseOpts
from .video_editor import ProcessVideo

def _real_main(argv=None):
    print(argv[1])
    opts = parseOpts(argv)

    print(opts.auto)
    print(opts.length)
    ProcessVideo(argv[1]+'.mp4', opts)


def main(argv=None):
    _real_main(argv)
