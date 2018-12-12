"""
Module which provides functionality for program arguments.
"""
import melog, optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-a", "--address", dest="address", help="address to translate into geo-coordinates")

    args = parser.parse_args()

    melog.info("program args: %s", args)

    return args


