import os
import tkFileDialog

import tkinter as tk
import tkMessageBox
import Patcher
import VivaldiPathFinder as path

class ConfigLoader(tk.Frame):

    def __init__(self, root):
        self.configfilename = "VivaldiThemeLoader.data"
        self.root = root
        self.options = {}

    def load(self):
        if self._configfileiscreated():
            self._readoptions()
        else:
            self._createconfigfile()

        Patcher.patchifnot(self.options["vivaldiFolder"], self.options["vivaldiThemeFolder"])

    def _configfileiscreated(self):
        return self.configfilename in os.listdir(os.getcwd())

    def _readoptions(self):
        try:
            config = open(os.getcwd() + "/" + self.configfilename, 'r')
            lines = [line.rstrip('\n') for line in config.readlines()]

            if len(lines) != 2:
                tkMessageBox.showerror("Error reading configuration", "Config file is corrupted")

            self.options["vivaldiFolder"] = lines[0]
            self.options["vivaldiThemeFolder"] = lines[1]

            config.close

        except Exception as e:
            tkMessageBox.showerror("Error reading configuration", "Can\'t open config file\n\n" + str(e))
            print e
            exit(1)

    def _createconfigfile(self):
        path_finder = path.VivaldiPathFinder(self.root)
        self.options["vivaldiFolder"] = path_finder.finddirectory()
        self.options["vivaldiThemeFolder"] = tkFileDialog.askdirectory(parent=self.root,
            title='Select a folder to save themes and scripts', initialdir=os.getcwd())

        self._writeconfigfile()

    def _writeconfigfile(self):
        config = open(self.configfilename, "w")
        config.write(self.options["vivaldiFolder"]+"\n")
        config.write(self.options["vivaldiThemeFolder"])
        config.close()


