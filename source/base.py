"""
Copyright (C) 2019  Andrew Shen

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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

