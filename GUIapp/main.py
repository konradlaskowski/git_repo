import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()

root.geometry("200x250")
root.resizable(False,False)
root.title('Oś Budżetu')
var = StringVar()
root.iconbitmap('budget.ico')
var.set('hello')

var2 = StringVar()



class Label_Textbox():
    def __init__(self, name):
        self.LbTB = StringVar()
        self.label = tkinter.Label(root, text=name)
        self.label.pack()
        self.name = name
        self.entry = tkinter.Entry(root, width=30, textvariable=self.LbTB)
        self.entry.pack()

    def print_var(self):
        self.var = self.LbTB.get()
        print(f'{self.name}: {self.var}')



amount = Label_Textbox('Kwota')
category = Label_Textbox('Kategoria')
which_store = Label_Textbox('Gdzie')
date = Label_Textbox('Data')
descr = Label_Textbox('Opis')




def funkcjaPrzycisku():

    amount.print_var()
    category.print_var()
    which_store.print_var()
    date.print_var()
    descr.print_var()
    messagebox.showinfo("Oś Budżetu: Success", "Twoje dane zostały przesłane do Google")


b = tkinter.Button(
    root,
    text="Wyślij",
    width=15,
    bg="green",
    fg="white",
    command=funkcjaPrzycisku,
)
b.place(x=10, y=210, width=180, height=30)







root.mainloop()