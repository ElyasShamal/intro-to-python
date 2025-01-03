


import tkinter


class TestAVG:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # create five frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        # create and pack the widget for test one 

        self.test1_label = tkinter.Label(self.test1_frame, text='Enter the score for test 1:')
        self.test1_entry = tkinter.Entry(self.test1_frame, width=20)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # create and pack the widget for test two
        self.test2_label = tkinter.Label(self.test2_frame, text='Enter the score for test 2:')
        self.test2_entry = tkinter.Entry(self.test2_frame, width=20)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # create and pack widget for test three
        self.test3_label = tkinter.Label(self.test3_frame, text='Enter the score for test 3:')
        self.test3_entry = tkinter.Entry(self.test3_frame, width=20)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        #  create and pack widget for the average.

        self.result_label = tkinter.Label(self.avg_frame, text='Average')
        self.avg = tkinter.StringVar()
        self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # create and pack the button widgets

        self.cal_button = tkinter.Button(self.button_frame, text='Average', command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit!', command=self.main_window.destroy)
        self.cal_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames 
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calc_avg(self):
        try:
            test1 = float(self.test1_entry.get())
            test2 = float(self.test2_entry.get())
            test3 = float(self.test3_entry.get())
            average = (test1 + test2 + test3) / 3.0
            self.avg.set(f"{average:.2f}") 
        except ValueError:
            self.avg.set("Invalid input!")  


if __name__ == '__main__':
    TestAVG()    