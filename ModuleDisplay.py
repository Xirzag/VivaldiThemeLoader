import tkinter as tk

def display(root, plugins):
    number_of_cols = 3
    row = 0
    plugins_without_add = len(plugins)
    while plugins_without_add != 0:
        for i in range(number_of_cols):
            if plugins_without_add == 0:
                break

            current_plugin = plugins[len(plugins) - plugins_without_add]
            current_plugin.attach_tk_instance(root)

            plugin_btn = tk.Button(root, text=current_plugin.name,
                command=current_plugin.call_plugin,
                height="150", width="150",
                image=current_plugin.img, anchor=tk.CENTER, compound=tk.TOP)

            plugin_btn.grid(row=row, column=i)
            plugins_without_add -= 1

        row += 1
