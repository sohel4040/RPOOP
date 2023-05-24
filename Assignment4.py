# for displaying two labels on the window
import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Sohel", bg="blue", fg="white", width=10, height=5)
label1.pack()

label2 = tk.Label(window, text="Bargir", bg="red", fg="white", width=7, height=3)
label2.pack()

window.mainloop()