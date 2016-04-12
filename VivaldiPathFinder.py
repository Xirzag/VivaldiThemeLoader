import tkinter as Tkinter
import tkFileDialog
import sys
import os
import tkMessageBox

COMMONCSS_PATH = "/resources/vivaldi/style/common.css"
STYLE_FOLDER_PATH = "/resources/vivaldi/style"

class VivaldiPathFinder(Tkinter.Frame):

    def __init__(self):
        Tkinter.Frame.__init__(self)

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = os.getcwd()
        options['mustexist'] = False
        options['title'] = 'Search Vivaldi user folder'
        #self.pack();

    def is_a_vivaldi_folder(self, path):
        try:
            return "common.css" in os.listdir(path + STYLE_FOLDER_PATH)
        except:
            return False


    def user_close_window(self, folder_path):
        return folder_path == ''

    def find_directory(self):
        folder_path = tkFileDialog.askdirectory(**self.dir_opt)

        while not self.is_a_vivaldi_folder(folder_path):
            if self.user_close_window(folder_path):
                sys.exit(1)

            tkMessageBox.showerror("Error searching Vivaldi folder","That isn\'t a Vivaldi folder")
            self.dir_opt['initialdir'] = folder_path
            folder_path = tkFileDialog.askdirectory(**self.dir_opt)



        return folder_path




