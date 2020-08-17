import optparse

def parseOpts(arguments=None):
    parser = optparse.OptionParser()
    parser.add_option("-a", action="store_true", dest="auto")
    parser.add_option("--auto", action="store_true", dest="auto")
    parser.add_option("-w", action="store_true", dest="webm")
    parser.add_option("--webm", action="store_true", dest="webm")
    parser.add_option("-g", action="store_true", dest="gif")
    parser.add_option("--gif", action="store_true", dest="gif")
    parser.add_option("-l", action="store", dest="length", nargs=3)
    parser.add_option("--length", action="store", dest="length", nargs=3)
    parser.add_option("-c", action="store", dest="clips")
    parser.add_option("--clips", action="store", dest="clips")

    parser.set_defaults(auto=False,
                        length=(10, 4, 0),
                        webm=False,
                        gif=False,
                        clips=None)

    opts,args = parser.parse_args(arguments)
    return opts