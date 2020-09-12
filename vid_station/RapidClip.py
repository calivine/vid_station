from .video import ImportVideo, Scene, Webm
from .utils import form_clip_list


class RapidClip:

    def __init__(self, options):
        """Clip video according to options.

        Parameters
        -------------
        options:Dict,
            Dictionary of options to tell
            RapidClip how to process.
        """
        self.options = options['opts']
        self.source = options['source']

    def process(self):
        """
        """
        # os.chdir(SOURCE_DIR)
        if self.options.auto:
            source_file = ImportVideo(self.source)
            # Generate series of timestamps to based edits to source file on.
            timestamps = source_file.make_time_stamps(int(self.options.length[0]), self.options.length[1], int(self.options.buffer))
            if self.options.verbose:
                print(timestamps)
                print(int(self.options.length[0]), self.options.length[1], int(self.options.buffer))
            source = Scene(self.source, timestamps).create()
        if self.options.clips is not None:
            clip_list = form_clip_list(self.options.clips)
            source = Scene(self.source, clip_list).create()
        if self.options.webm:
            Webm(self.source)
        if self.options.gif:
            GIF(self.source)
