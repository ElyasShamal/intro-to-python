

import tkinter
import tkinter.messagebox


class Button:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.myButton = tkinter.Button(self.main_window, text='ClickMe!', command=self.do_something)

        self.myButton.pack()
        tkinter.mainloop()


    def do_something(self):
        tkinter.messagebox.showinfo("Response", "Thanks for Clicking the button")    

if __name__ == '__main__':
    myGui = Button()