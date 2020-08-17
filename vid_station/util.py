import random


def generate_filename(source):
    return "comp{}_{}".format(str(random.randint(1, 10000)), source)


def form_clip_list(input):
    clip_list = []
    print(input)
    clip_list_raw = input[1:-1]
    print(clip_list_raw)
    cll = clip_list_raw.split(",")
    print(cll)
    cll.reverse()
    print(cll)
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
    print(clip_list)
    return clip_list
