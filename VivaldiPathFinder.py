import tkinter as Tkinter
import tkFileDialog
import sys
import os
import tkMessageBox

COMMONCSS_PATH = "/resources/vivaldi/style/common.css"
STYLE_FOLDER_PATH = "/resources/vivaldi/style"

class VivaldiPathFinder(Tkinter.Frame):

    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)

        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = os.getcwd()
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Search Vivaldi user folder'
        self.pack();

    def isavivaldifolder(self, path):
        try:
            return "common.css" in os.listdir(path + STYLE_FOLDER_PATH)
        except:
            return False


    def userclosewindow(self, folder_path):
        return folder_path == ''

    def finddirectory(self):
        folder_path = tkFileDialog.askdirectory(**self.dir_opt)

        while not self.isavivaldifolder(folder_path):
            if self.userclosewindow(folder_path):
                sys.exit(1)

            tkMessageBox.showerror("Error searching Vivaldi folder","That isn\'t a Vivaldi folder")
            self.dir_opt['initialdir'] = folder_path
            folder_path = tkFileDialog.askdirectory(**self.dir_opt)



        return folder_path




