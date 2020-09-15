from .video import ImportVideo, Scene, Webm
from .utils import form_clip_list, add_extension


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
        if self.options.verbose:
            print(self.options)


    def process(self):
        """
        """
        # os.chdir(SOURCE_DIR)
        if self.options.auto:
            source_file = ImportVideo(self.source)
            # Generate series of timestamps to based edits to source file on.
            total_clips = int(self.options.length[0])
            clip_length = self.options.length[1]
            buffer = int(self.options.buffer)
            timestamps = source_file.make_time_stamps(total_clips, clip_length, buffer)
            if self.options.verbose:
                print(timestamps)
                print(total_clips, clip_length, buffer)
            source = Scene(self.source, timestamps).create()
        if self.options.clips is not None:
            clip_list = form_clip_list(self.options.clips)
            source = Scene(self.source, clip_list).create()
        if self.options.webm:
            Webm(self.source)
        if self.options.gif:
            GIF(self.source)

    def process_batch(self):
        f = open(self.options.batch, 'r')
        i = 0
        while True:
            line = f.readline()
            if not line:
                break
            self.source = add_extension(line[:-1])
            print(str(i), self.source)
            self.process()
            i += 1
        f.close()
