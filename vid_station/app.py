from .video import Clip, Webm, GIF
from .config import *
from .util import generate_filename, form_clip_list
from .video_editor import Scene

import sys
import os


def ProcessVideo(source, opts):
    os.chdir(SOURCE_DIR)
    if opts.auto:
        source_file = Clip(source)
        # Generate series of timestamps to based edits to source file on.
        timestamps = source_file.make_time_stamps(int(opts.length[0]), int(opts.length[1]), int(opts.buffer))
        source = Scene(source, timestamps).create()
    if opts.clips is not None:
        clip_list = form_clip_list(opts.clips)
        source = Scene(source, clip_list).create()
    if opts.webm:
        Webm(os.path.join('clips', source))
    if opts.gif:
        GIF(os.path.join('clips', source))
