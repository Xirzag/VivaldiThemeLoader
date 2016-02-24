import tkinter as tk
import sys
import ConfigLoader as conf

counter = 0


def main(argv=None):
    root = tk.Tk()
    config = conf.ConfigLoader(root)
    config.load();

    root.title("Vivaldi Theme Loader")
    label = tk.Label(root, fg="green", text="Patch succesfully applied")
    label.pack(padx=40, pady=20)

    root.mainloop()
    return 0


if __name__ == '__main__':
    status = main()
    sys.exit(status)
