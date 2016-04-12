import os
import tkMessageBox
import tkinter as tk
import VivaldiAPI as viv

class css_plugin():
    CSS_FOLDER = "css"

    def __init__(self, path, tk_instance):
        self.path = path

        self.check_box_state = {}
        self.root = tk.Toplevel()
        self.root.title("CSS")
        self.root.minsize(width=200, height=10)

        self.display()


    def update_css(self, theme):
        if self.check_box_state[theme].get() == 0:
            viv.remove_from_vivaldi_css(self.theme_path(theme))
        else:
            viv.add_to_vivaldi_css(self.theme_path(theme))


    def css_folder(self):
        return os.path.dirname(self.path) + "/" + self.CSS_FOLDER

    def refresh(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.display()

    def display(self):
        tk.Button(self.root, command=self.refresh, text="Refresh").grid(row=0)

        for index, theme in enumerate(os.listdir(self.css_folder())):
            self.check_box_state[theme] = tk.IntVar()
            self.check_box_state[theme].set(viv.vivaldi_have_css(self.theme_path(theme)))

            tk.Checkbutton(self.root, text=theme, variable=self.check_box_state[theme],
                           command=lambda theme=theme: self.update_css(theme), justify=tk.LEFT).grid(row=index+1, sticky=tk.W)

        self.root.mainloop()

    def theme_path(self, theme):
        return self.css_folder() + "/" + theme


def plugin_main(path, tk_instance):
    css_plugin(path, tk_instance)
