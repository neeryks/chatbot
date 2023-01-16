
import tkinter as tk
from process import Responder
from auth import auth

class Interfacer(Responder):
    def __init__(self) -> None:
        self.root = tk.Tk()

    def window_maker(self):
        self.root.title("Centuari Ai")
        self.root.geometry("1000x800")
        return 0

    def text_input(self):
        entr = tk.StringVar()
        entr_widget = tk.Entry(self.root,textvariable=entr)
        entr_widget.pack()
        return entr

    def result_display(self):
        data = self.text_complete(self.text_input())
        data = data.choices[0].text
        return print(data)

    def submit_button(self):
        submit = tk.Button(self.root,text="Submit",command=self.result_display)
        submit.pack()
        return 0

    def mainloop(self):
        return self.root.mainloop()


if __name__ =="__main__":
    auth()
    start = Interfacer()
    start.window_maker()
    start.submit_button()
    start.mainloop()


