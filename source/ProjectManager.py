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

import os
import configparser as config


class ProjectManager:
    FILE_LOG_DATA = []
    CONSTANT = {}

    def __init__(self, fname):
        self.fname = fname

        # load file if exist
        if os.path.isfile(fname+".gai"):
            with open(fname+".gai", "r") as fbj:
                fdt = fbj.readlines()

        # load .ini file
        cfg = config.ConfigParser()  # load config parser
        cfg.optionxform = str
        cfg.read("meta.ini")
        for sect in cfg.sections():
            ProjectManager.CONSTANT[sect] = {}
            for key, val in cfg.items(sect):  # test out each type; default is string
                if val.isdigit(): ProjectManager.CONSTANT[sect][key] = int(val)
                elif val == "true": ProjectManager.CONSTANT[sect][key] = True
                elif val == "false": ProjectManager.CONSTANT[sect][key] = False
                else: ProjectManager.CONSTANT[sect][key] = val

    @classmethod
    def insert_node(cls, pos, fx):
        cls.FILE_LOG_DATA.append(["%NODE", pos, fx])

    @classmethod
    def insert_bias(cls, nodes, weight):
        cls.FILE_LOG_DATA.append(["%BIAS", nodes[0], nodes[1], weight])

    def flush(self):  # write files from the log data
        with open(self.fname+".gai", "a") as fbj:
            pass

    class Mouse:
        @staticmethod
        def OnTrigger(first, last): return True if first != last and last is False else False  # useless


"""
flushed-based file
.gai File system:

%world posx posy
$var %node posx posy fx
$nodes %node posx posy fx
$var1 %bias node1 node2 weight


"""