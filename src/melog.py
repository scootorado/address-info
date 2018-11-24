"""
Module to wrap logging functionality to make it easier to change if ever needed.

Currently we are using pythons simple print() method.
"""


def info(msg, *args):
    __log(msg, args)


def error(msg, *args):
    msg = "----- ERROR ----- " + msg
    __log(msg, args)


def __log(msg, args):
    msg = msg % args
    print(msg)
