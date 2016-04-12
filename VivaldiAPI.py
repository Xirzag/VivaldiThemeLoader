
def add_to_vivaldi_css(css_path):
    custom_path = __api_config.custom_css_path()
    with open(custom_path, "a") as custom_css:
        custom_css.write("@import "+css_path+"\n")


def remove_from_vivaldi_css(css_path):
    custom_path = __api_config.custom_css_path()
    custom_css = open(custom_path, "r")
    lines = [line.rstrip('\n') for line in custom_css.readlines()]
    lines = filter(lambda css_line: css_path not in css_line, lines)
    custom_css.close()
    custom_css = open(custom_path, "w")
    custom_css.seek(0, 0)

    for line_to_write in lines:
        # print line_to_write
        custom_css.write(line_to_write + "\n")

    custom_css.close()


def vivaldi_have_css(css_path):
    custom_path = __api_config.custom_css_path()
    with open(custom_path, "r") as custom_css:
        return "@import " + css_path in [line.rstrip('\n') for line in custom_css.readlines()]



__api_config = 0
