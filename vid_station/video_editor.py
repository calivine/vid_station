from video import Clip, Webm, GIF, VideoEditor
from config import *
from .util import generate_filename

import sys
import os

def ProcessVideo(source, opts):
    os.chdir(SOURCE_DIR)
    if opts.auto:
        source_file = Clip(source)
        timestamps = source_file.make_time_stamps(int(opts.length[0]), int(opts.length[1]), int(opts.length[2]))
        to_be_processed = []
        for c in timestamps:
            new_clip = Clip(source, c[0], c[1])
            to_be_processed.append(new_clip.clip)

        ve = VideoEditor()
        source = generate_filename(source)
        ve.paste_clips(source, to_be_processed)
    if opts.webm:
        print(source)
        Webm(os.path.join('clips', source))
    if opts.gif:
        GIF(os.path.join('clips', source))
