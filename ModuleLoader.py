import os
import tkMessageBox
import json
import imp
from Tkinter import PhotoImage, Image


class Module:

    def __init__(self, name, photo, execute_file):
        self.img = PhotoImage(name=name, file=photo)
        self.name = name
        self.main = execute_file

    def attach_tk_instance(self, root):
        self.root = root

    def call_plugin(self):
        plugin = imp.load_source(self.name, self.main)
        plugin.plugin_main(path=self.main, tk_instance=self.root)


MANIFEST_FILE = "manifest.txt"

NO_PHOTO_NAME = "noPhoto.png"
NO_PHOTO_PATH = NO_PHOTO_NAME


def get_modules_from(plugin_folder):
    plugins_folders = os.walk(plugin_folder).next()[1]
    modules = []
    for folder in plugins_folders:
        try:
            with open(plugin_folder + "/" + folder + "/" + MANIFEST_FILE) as manifest:
                plugin_path = plugin_folder + "/" + folder
                data = json.load(manifest)

                plugin_img_path = plugin_path + "/" + data["image"]
                plugin_img = plugin_img_path if os.path.exists(plugin_img_path) else "none"

                modules.append(Module(data["name"], plugin_img, plugin_path + "/" + data["execute"]), )
        except Exception as e:
            tkMessageBox.showerror("Error loading plugin", "Can't load plugin in " + folder + " \n\n"
                                   + str(e))

    return modules
