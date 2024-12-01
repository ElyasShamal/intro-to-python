

import tkinter


class MyGuI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        # create new label wodget
        self.label = tkinter.Label(self.main_window, text='Hello world')
        self.label.pack()

        tkinter.mainloop()

if __name__ == "__main__":
    my_gui = MyGuI()