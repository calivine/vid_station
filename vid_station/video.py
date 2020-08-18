from moviepy.editor import *
import os
import random

class Clip:

    VIDEO_SIZES = {
        '60.0': {
            '1080': '13000',
            '720': '6500',
            '640': '4600',
            '540': '4500',
            '360': '3000'
        },
        '30.0': {
            '1080': '7000',
            '720': '3500',
            '640': '3250',
            '568': '3000',
            '540': '2500',
            '480': '2250',
            '360': '2000'
        },
        '25.0': {
            '1080': '6500',
            '720': '3250',
            '640': '3000',
            '540': '2250',
            '408': '2000',
            '360': '2000'
        },
        '24.0': {
            '1080': '6000',
            '720': '3000',
            '640': '2500',
            '540': '2000',
            '360': '2000'
        }
    }

    def __init__(self, source, start=None, end=None):
        """Create a Clip of a Video.

        Parameters
        -------------
        source:String,
            Source file or path.
        start:Integer,
            Starting position of clip in seconds.
        end:Integer,
            Ending position of clip in seconds.
        """
        self.source = source
        self.clip = VideoFileClip(source).subclip(self._format_ts(start), self._format_ts(end)) if start is not None else VideoFileClip(source)
        self.fps = round(self.clip.fps, 0)
        self.bitrate = self.VIDEO_SIZES[str(self.fps)][str(self.clip.h)] + 'k'
        #if start is not None:
        #    dest = self._save('{}{}_c_{}'.format(start, end, source))
        #    self.clip = VideoFileClip(dest)

    def _save(self, dest):
        """Save Clip of a Video file

        Parameters
        -------------
        dest:String,
            Destination file or path.
        """
        if not os.path.exists('clips'):
            os.mkdir('clips')

        try:
            self.clip.write_videofile(os.path.join('clips', dest), bitrate=self.bitrate)
            self.clip.close()
        except OSError:
            print('OSError')
        return dest

    def _format_ts(self, ts):
        """Convert timestamp from MM:SS to total seconds

        Parameters
        -------------
        ts:Timestamp
            Timestamp to be converted
        """
        if ':' in str(ts):
            timestamp = ts.split(':')
            return int(timestamp[0]) * 60 + int(timestamp[1])
        else:
            return ts

    def make_time_stamps(self, amount, length, buffer):
        """Generate set of timestamps

        Parameters
        -------------
        amount:Integer
            Total number of clips to make.
        length:Integer
            Length of each clip.
        buffer:Integer
            Begin grabbing timestamps BUFFER seconds into clip.
        """
        timestamps = []
        duration = self.clip.duration
        frequency = (duration // amount)-3
        i = 0 + buffer
        while i < duration:
            i += frequency
            if i >= duration:
                break
            length = int(length) if length != 'r' else random.randrange(1, 5)
            timestamps.append([i, i+length])
        return timestamps


class Webm(Clip):

    def __init__(self, source, start=None, end=None):
        """Make webm file with source video.

        :param source: source video file to convert to mp4
        :param start: if provided, start of clip to convert
        :param end: if provided, end of clip to convert
        """
        Clip.__init__(self, source, start, end)
        self._save_webm()

    def _save_webm(self):
        if not os.path.exists('webm'):
            os.mkdir('webm')

        self.clip.write_videofile(os.path.join('webm', self.clip.filename[6:-4]+'.webm'), fps=int(self.fps), bitrate=self.bitrate)
        self.clip.close()


class GIF(Clip):

    def __init__(self, source, start=None, end=None):
        Clip.__init__(self, source, start, end)
        self._save_gif()

    def _save_gif(self):
        if not os.path.exists('gif'):
            os.mkdir('gif')
        resized_clip = self.clip.resize(width=480)
        resized_clip.write_gif(os.path.join('gif', self.clip.filename[6:-4]+'.gif'), fps=int(self.fps))

        self.clip.close()


class VideoEditor:

    def __init__(self):
        if not os.path.exists('clips'):
            os.mkdir('clips')

    def paste_clips(self, destination, clips):
        """Concatenate clips together into one.
        """
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(os.path.join('clips', destination))
        final_clip.close()
