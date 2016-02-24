import tkMessageBox
import VivaldiPathFinder as path


def patchifnot(vivaldi_folder, vivaldi_theme_folder):
    _patchvivaldi(vivaldi_folder, vivaldi_theme_folder)
    _patchthemefolder(vivaldi_theme_folder)


_THEME_FILE = "custom.css"


def _patchstyle(common, vivaldithemefolder):
    common.seek(0, 0)
    content = common.read()
    common.seek(0, 0)
    common.write("/* Vivaldi Theme Loader */\n"
                 "@import " + vivaldithemefolder + "/" + _THEME_FILE + "\n"
                 + content)


def _patchthemefolder(vivaldi_theme_folder):
    try:
        open(vivaldi_theme_folder+"/" + _THEME_FILE, 'a').close()
    except Exception as e:
        tkMessageBox.showerror("Error checking theme file",
                               "Can't open or create theme file\n\n"
                               + str(e))
        exit(2)


def _patchvivaldi(vivaldi_folder, vivaldi_theme_folder):
    try:
        common = open(vivaldi_folder + path.COMMONCSS_PATH, "rw+")
        firstline = common.readline().rstrip('\n')

        if firstline != "@import " + vivaldi_theme_folder + "/" + _THEME_FILE:
            _patchstyle(common, vivaldi_theme_folder)

        common.close()

    except Exception as e:
        tkMessageBox.showerror("Error patching Vivaldi", "Can't patch Vivaldi style \n"
                               "Maybe you should execute the script with root or admin\n\n"
                               + str(e))
        exit(2)