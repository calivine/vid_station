import os
import sys


from .options import parseOpts
from .video_editor import ProcessVideo


def _real_main(argv=None):
    opts = parseOpts(argv)
    ProcessVideo(argv[1]+'.mp4', opts)


def main(argv=None):
    _real_main(argv)
