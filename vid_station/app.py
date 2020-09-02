import os

from .video import Clip, Webm, GIF
from .config import *
from .video_editor import Scene


def form_clip_list(inpt):
    clip_list = []
    clip_list_raw = inpt[1:-1]
    cll = clip_list_raw.split(",")
    cll.reverse()
    st = True
    while len(cll) > 0:
        ts = cll.pop()
        if st:
            start = ts
            st = False
        else:
            end = ts
            st = True
            clip_list.append([start, end])
    return clip_list


def process_video(source, opts):
    os.chdir(SOURCE_DIR)
    if opts.auto:
        source_file = Clip(source)
        # Generate series of timestamps to based edits to source file on.
        timestamps = source_file.make_time_stamps(int(opts.length[0]), opts.length[1], int(opts.buffer))
        source = Scene(source, timestamps).create()
    if opts.clips is not None:
        clip_list = form_clip_list(opts.clips)
        source = Scene(source, clip_list).create()
    if opts.webm:
        Webm(os.path.join('clips', source))
    if opts.gif:
        GIF(os.path.join('clips', source))
