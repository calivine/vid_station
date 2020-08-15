import random

def generate_filename(source):
    return "comp{}_{}".format(str(random.randint(1, 10000)), source)
