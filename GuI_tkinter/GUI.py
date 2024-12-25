


import tkinter
import tkinter.font


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # create canvas widget.
        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)
        myFont = tkinter.font.Font(family='Helvetica', size=18, weight='bold')

        self.canvas.create_text(50, 50, text='Hello Elyas Shamal', font=myFont)
        self.canvas.pack()
        tkinter.mainloop()

if __name__ == '__main__':
    gui = GUI()
