import os
import tkMessageBox
import VivaldiPathFinder as path


def patch_if_not(config):
    _patch_vivaldi(config)
    _patch_config_folder(config)


def _patch_style(common, config):
    common.seek(0, 0)
    content = common.read()
    common.seek(0, 0)
    common.write("/* Vivaldi Theme Loader */\n"
                 "@import " + config.custom_css_path() + "\n"
                 + content)


def _patch_config_folder(config):
    try:
        open(config.custom_css_path(), 'a').close()
        try_create_plugin_folder(config)
    except Exception as e:
        tkMessageBox.showerror("Error checking theme file",
                               "Can't open or create theme file\n\n"
                               + str(e))
        exit(2)


def try_create_plugin_folder(config):
    try:
        os.mkdir(config.plugins_folder_path())
    except:
        pass


def _patch_vivaldi(config):
    try:
        common = open(config.common_css_path(), "rw+")
        firstline = common.readline().rstrip('\n')

        if firstline != "@import " + config.custom_css_path():
            _patch_style(common, config)

        common.close()

    except Exception as e:
        tkMessageBox.showerror("Error patching Vivaldi", "Can't patch Vivaldi style \n"
                               "Maybe you should execute the script with root or admin\n\n"
                               + str(e))
        exit(2)