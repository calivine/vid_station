import random

from .video import Clip, VideoEditor


def generate_filename(source):
    return "comp{}_{}".format(str(random.randint(1, 10000)), source)


def _fill_clip_list(source, ts):
    to_be_processed = []
    for c in ts:
        new_clip = Clip(source, c[0], c[1])
        to_be_processed.append(new_clip.clip)
    return to_be_processed


class Scene:

    def __init__(self, source, timestamps):
        self.source = source
        self.clips = _fill_clip_list(source, timestamps)

    def create(self):
        ve = VideoEditor()
        new_file = generate_filename(self.source)

        ve.paste_clips(new_file, self.clips)
        return new_file
