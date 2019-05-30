from tkinter import *

class keys_dispenser(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Keys Batch").grid(row=0,column=1, sticky=E)
        self.batch_no=Entry(self, width=20)
        self.batch_no.grid(row=0, column=2, columnspan=2, sticky=W)
        Button(self, text="hohoho", command=self.get_key, width=10).grid(row=1, column=2, sticky=W)
        Button(self, text="rororo", command=self.exit, width=10).grid(row=1, column=3, columnspan=2, sticky=W)
        Label(self, text="Key").grid(row=2,column=1, sticky=E)
        self.answer=Text(self, width=25, height=1, wrap=WORD)
        self.answer.grid(row=2, column=2, columnspan=2, sticky=W)

    def get_key(self):
        try:
            self.answ=int(self.batch_no.get())
            self.answ=str(self.batch_no.get())
        except ValueError:
            self.answ="Key was not chosen"
        self.key_display()

    def exit(self):
            root.destroy()

    def key_display(self):
        self.answer.delete(0.0,END)
        self.answer.insert(0.0,self.answ)
        self.batch_no.delete(0, END)

root=Tk()
root.title("Keys Dispenser")
keys_dispenser=keys_dispenser(root)
root.mainloop()
