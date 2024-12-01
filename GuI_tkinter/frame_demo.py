
# create two frame one for top one for bottom 
# create three labels for top Frame.
# pack the labels that are in the top frame.
# stock the label one on the top of other

# create three label wedgets for the bottom frame 
# stock the label one on the top of other

import tkinter

class Frame:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # frame one
        self.label1 = tkinter.Label(self.top_frame, text='Winken')
        self.label2 = tkinter.Label(self.top_frame, text='Blinken')
        self.label3 = tkinter.Label(self.top_frame, text='Nod')
        # frame one labels
        self.label1.pack(side='top', pady=(50, 0))
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        # labels for frame 2
        self.label4 = tkinter.Label(self.bottom_frame, text='Winken bottom')
        self.label5 = tkinter.Label(self.bottom_frame, text='Blinken bottom')
        self.label6 = tkinter.Label(self.bottom_frame, text='Nod bottom')
        # stock at the top of each other
        
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        # pack the frames 

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    frame = Frame()        




