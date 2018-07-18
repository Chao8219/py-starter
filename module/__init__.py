import tkinter as tk


class MainGUI(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.frame = tk.Frame
        self.parent = parent
        parent.title("This is a title")


root = tk.Tk()
My_GUI = MainGUI(root)
My_GUI.pack()
root.mainloop()