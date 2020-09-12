def add_extension(source, ext=".mp4"):
    if source.endswith(".mp4"):
        return source
    elif source.endswith(".avi"):
        return source
    elif source.endswith(".mov"):
        return source
    elif source.endswith(".wmv"):
        return source
    else:
        return source + ext

def process_batch(opts):
    f = open(opts.batch, 'r')
    i = 0
    while True:
        line = f.readline()
        if not line:
            break
        filename = add_extension(line[:-1])
        print(str(i), filename)
        process_video(filename, opts)
        i += 1
    f.close()

def form_clip_list(inpt):
    """Serialize custom timestamp option.

    """
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
