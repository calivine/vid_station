import datetime
import random

from dateutil import tz

from moviepy.editor import *

# Change class name to ImportVideo.

class ImportVideo:

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
            '384': '2100',
            '360': '2000',
            '352': '1990',
            '320': '1850',
            '240': '1800',
        },
        '25.0': {
            '1080': '6500',
            '720': '3250',
            '640': '3000',
            '540': '2250',
            '480': '2000',
            '408': '2000',
            '392': '2000',
            '360': '2000'
        },
        '24.0': {
            '1080': '6000',
            '720': '3000',
            '640': '2500',
            '540': '2000',
            '480': '2000',
            '360': '2000',
            '352': '1990',
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
        start = self._format_ts(start)
        end = self._format_ts(end)
        self.source = source
        self.clip = VideoFileClip(source).subclip(start, end) if start is not None else VideoFileClip(source)
        self.fps = round(self.clip.fps, 0)
        self.bitrate = self.VIDEO_SIZES[str(self.fps)][str(self.clip.h)] + 'k'
        # if start is not None:
        #    dest = self._save('{}{}_c_{}'.format(start, end, source))
        #    self.clip = VideoFileClip(dest)

    def _save(self, dest):
        """Save Clip of a Video file

        Parameters
        -------------
        dest:String,
            Destination file or path.
        """

        try:
            self.clip.write_videofile(dest, bitrate=self.bitrate)
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
        while i < duration-5:
            i += frequency
            if i >= duration-5:
                break
            length = int(length) if length != 'r' else random.randrange(1, 5)
            timestamps.append([i, i+length])
        return timestamps


class Webm(ImportVideo):

    def __init__(self, source, start=None, end=None):
        """Make webm file with source video.

        :param source: source video file to convert to mp4
        :param start: if provided, start of clip to convert
        :param end: if provided, end of clip to convert
        """
        Clip.__init__(self, source, start, end)
        self._save_webm()

    def _save_webm(self):
        output = self.clip.filename[6:-4]+'.webm'
        self.clip.write_videofile(output, fps=int(self.fps), bitrate=self.bitrate)
        self.clip.close()


class GIF(ImportVideo):

    def __init__(self, source, start=None, end=None):
        Clip.__init__(self, source, start, end)
        self._save_gif()

    def _save_gif(self):
        resized_clip = self.clip.resize(width=480)
        output = self.clip.filename[6:-4]+'.gif'
        resized_clip.write_gif(output, fps=int(self.fps))
        self.clip.close()


def paste_clips(destination, clips):
    """Concatenate clips.
    """
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(destination[6:-4]+'.mp4')
    final_clip.close()
    # Close open clip connections.
    for clip in clips:
        clip.close()


def generate_filename(source):
    localzone = tz.gettz()
    localzone.tzname(datetime.datetime.now())
    now = datetime.datetime.now()
    iso = now.replace(tzinfo=localzone).isoformat()
    mask = "".join(iso.split('T')[1].replace(':', '').replace('.', '').split('-'))
    return "{}_{}".format(mask, source)


def _fill_clip_list(source, ts):
    to_be_processed = []
    for c in ts:
        new_clip = ImportVideo(source, c[0], c[1])
        to_be_processed.append(new_clip.clip)
    return to_be_processed


class Scene:

    def __init__(self, source, timestamps):
        self.source = source
        self.clips = _fill_clip_list(source, timestamps)

    def create(self):
        new_file = generate_filename(self.source)

        paste_clips(new_file, self.clips)
        return new_file[6:-4]+'.mp4'
