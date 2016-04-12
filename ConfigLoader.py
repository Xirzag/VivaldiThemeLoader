import os
import tkFileDialog
import tkinter as tk
import tkMessageBox

import Patcher
import VivaldiPathFinder as path
import VivaldiAPI as viv


class ConfigLoader(tk.Frame):

    def __init__(self):
        self.configfilename = "VivaldiThemeLoader.data"
        self.option = {}

    def load(self):
        if self._config_file_is_created():
            self._read_options()
        else:
            self._create_config_file()
        viv.__api_config = self

        Patcher.patch_if_not(self)

    def custom_css_path(self):
        return self.option["vivaldiThemeFolder"] + "/custom.css"

    def plugin_folder_path(self):
        return self.option["vivaldiThemeFolder"] + "/plugins"

    def vivaldi_folder_path(self):
        return self.option["vivaldiFolder"]

    def vivaldi_config_folder_path(self):
        return self.option["vivaldiThemeFolder"]

    def common_css_path(self):
        return self.option["vivaldiFolder"] + "/resources/vivaldi/style/common.css"

    def _config_file_is_created(self):
        return self.configfilename in os.listdir(os.getcwd())

    def _read_options(self):
        try:
            config = open(os.getcwd() + "/" + self.configfilename, 'r')
            lines = [line.rstrip('\n') for line in config.readlines()]

            if len(lines) != 2:
                tkMessageBox.showerror("Error reading configuration", "Config file is corrupted")

            self.option["vivaldiFolder"] = lines[0]
            self.option["vivaldiThemeFolder"] = lines[1]

            config.close()

        except Exception as e:
            tkMessageBox.showerror("Error reading configuration", "Can\'t open config file\n\n" + str(e))
            print(e)
            exit(1)

    def _create_config_file(self):
        path_finder = path.VivaldiPathFinder()
        self.option["vivaldiFolder"] = path_finder.find_directory()
        self.option["vivaldiThemeFolder"] = tkFileDialog.askdirectory(
            title='Select a folder to save themes and scripts', initialdir=os.getcwd())

        self._write_config_file()

    def _write_config_file(self):
        config = open(self.configfilename, "w")
        config.write(self.option["vivaldiFolder"] + "\n")
        config.write(self.option["vivaldiThemeFolder"])
        config.close()


