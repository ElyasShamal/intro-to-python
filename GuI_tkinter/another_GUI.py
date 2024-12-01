 

# internal padding  ipadx , ipady
# external padding, padx , pady

import tkinter

class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Introduction')
        self.label_one = tkinter.Label(self.main_window, text="Hello world!", borderwidth=1, relief='solid')
        self.label_two = tkinter.Label(self.main_window, text='This is my first GUI', borderwidth=1, relief='ridge')

        self.label_one.pack(side='left', ipadx=20, ipady=20)
        self.label_two.pack(side='left', ipadx=20, ipady=20)
        tkinter.mainloop()

if __name__ == "__main__":
    gui = GUI()