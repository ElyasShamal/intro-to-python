


import tkinter
import tkinter.messagebox


class KiloConventerGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distence in kilometers: ')
        # create a input box for user input 
        self.kilo_entery = tkinter.Entry(self.top_frame, width=10)
        self.prompt_label.pack(side='left')
        self.kilo_entery.pack(side='left')
        # create buttons for buttom frame 
        self.cal_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_buttom = tkinter.Button(self.bottom_frame, text='Quit!', command=self.main_window.destroy)
        self.cal_button.pack(side='left')
        self.quit_buttom.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entery.get())
        miles = kilo * 0.6214
        tkinter.messagebox.showinfo('Result', str(kilo) + ' Kilometers is equal to ' + str(miles) + ' miles')

if __name__ == '__main__':
    kilo_conv = KiloConventerGUI()




