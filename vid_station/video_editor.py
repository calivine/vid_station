from .video import Clip, VideoEditor
from .util import generate_filename


class Scene:

    def __init__(self, source, timestamps):
        self.source = source
        self.clips = self._fill_clip_list(source, timestamps)

    def _fill_clip_list(self, source, ts):
        to_be_processed = []
        for c in ts:
            new_clip = Clip(source, c[0], c[1])
            to_be_processed.append(new_clip.clip)
        return to_be_processed

    def create(self):
        ve = VideoEditor()
        new_file = generate_filename(self.source)

        ve.paste_clips(new_file, self.clips)
        return new_file
