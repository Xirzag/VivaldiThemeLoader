import tkinter as tk
import sys
import ConfigLoader as conf
import ModuleLoader as plugin
import ModuleDisplay
import VivaldiAPI as viv

counter = 0


def main(argv=None):

    config = conf.ConfigLoader()
    root = tk.Tk()
    config.load();
    viv.__api_config = config

    root.title("Vivaldi Theme Loader")
    #root.geometry("530x320")

    plugins = plugin.get_modules_from(config.option["vivaldiThemeFolder"] + "/plugins")

    ModuleDisplay.display(root, plugins)
    root.mainloop()

    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
