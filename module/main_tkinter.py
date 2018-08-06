import tkinter as tk


class ScriptFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.script = tk.Text(parent, height=10, width=10)
        self.script.insert("end", "abc")
        self.place(anchor="nw", x=10, y=10)
        self.script.pack()



class MainFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent  # parent is the main window
        parent.title("Take A New Adventure")
        parent.geometry('810x500')  # 0.618 ratio
        parent.resizable(width=False, height=False)  # non-changeable fame.

        #self.script_main = ScriptFrame(parent, bg="green")
        #self.script_main.pack()

        self.label = tk.Label(parent, text="This is a GUI label")
        self.label.pack(side="bottom")
        self.close_button = tk.Button(parent, text="Close", command=parent.quit)
        self.close_button.pack(side="top")


root = tk.Tk()
main_frame = MainFrame(root, height=100, width=100)
main_frame.pack()
root.mainloop()