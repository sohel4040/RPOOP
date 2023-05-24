import tkinter as tk

window = tk.Tk()

def menu_click():
    print("Menu item clicked!")

menu_bar = tk.Menu(window)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=menu_click)
file_menu.add_command(label="Save", command=menu_click)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=menu_click)
edit_menu.add_command(label="Copy", command=menu_click)
edit_menu.add_command(label="Paste", command=menu_click)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

window.config(menu=menu_bar)

window.mainloop()
