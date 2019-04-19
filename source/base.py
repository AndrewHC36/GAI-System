# base functionality

class Error(Exception): # Base Error Class for all of this software
    __module__ = Exception.__module__
    def __init__(self, e):
        self.e = e

    def __str__(self):
        return "\n\t {}".format(self.e)


class BaseWarning:
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return "Warning: \n\t {}".format(self.s)


def check_args(ind, default, *args): return default if len(args) > ind else args[ind]

def on_trigger(first, last): return True if first != last and last is False else False

