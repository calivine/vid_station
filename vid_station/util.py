import random


def generate_filename(source):
    return "comp{}_{}".format(str(random.randint(1, 10000)), source)


def add_extension(source, ext=".mp4"):
    if source.endswith(".mp4"):
        return source
    else:
        return source + ext


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
