from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk

from ResourceNR import ResourceNR

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("5G NR Throughput Calculator")
        self.root.configure(background="blue")
        self.root.geometry("440x350")
        self.root.iconbitmap("img/venda1.ico")
        self.root.resizable(False, False)

        self.backGroundImage = PhotoImage(file="img/background.png")
        self.label = Label(self.root, image=self.backGroundImage)
        self.label.place(x=0, y=0)
        self.label.image = self.backGroundImage

        # Parâmetros de Entrada

        self.inputFrame = LabelFrame(self.root, text='Input Parameters', width=390, height=190, font=('TkDefaultFont', 12, "bold"))
        self.inputFrame.grid(row=0, column=0, padx=25, pady=25)

        # Caixas de escolha

        self.testLabel = Label(self.inputFrame, text='FR', wraplength=245, anchor=W)
        self.testLabel.place(x=60, y=10)
        self.frChosen = StringVar()
        self.frChoose = ttk.Combobox(self.inputFrame, textvariable=self.frChosen, width=10)
        self.frChoose['values'] = ['FR1', 'FR2']
        self.frChoose.place(x=30, y=30)

        self.testLabel = Label(self.inputFrame, text='BW', wraplength=245, anchor=W)
        self.testLabel.place(x=180, y=10)
        self.bwChosen = StringVar()
        self.bwChoose = ttk.Combobox(self.inputFrame, textvariable=self.bwChosen, width=10)
        self.bwChoose['values'] = ['5 MHz','10 MHz', '15 MHz', '20 MHz', '25 MHz', '30 MHz', '40 MHz', '50 MHz', '60 MHz', '80 MHz', '90 MHz', '100 MHz']
        self.bwChoose.place(x=150, y=30)

        self.testLabel = Label(self.inputFrame, text='CA', wraplength=245, anchor=W)
        self.testLabel.place(x=300, y=10)
        self.cpChosen = StringVar()
        self.cpChoose= ttk.Combobox(self.inputFrame, textvariable=self.cpChosen, width=10)
        self.cpChoose['values'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.cpChoose.place(x=270, y=30)

        self.testLabel = Label(self.inputFrame, text='SCS', wraplength=245, anchor=W)
        self.testLabel.place(x=57, y=70)
        self.scsChosen = StringVar()
        self.scsChoose= ttk.Combobox(self.inputFrame, textvariable=self.scsChosen, width=10)
        self.scsChoose['values'] = ['15 MHz', '30 MHz', '60 MHz']
        self.scsChoose.place(x=30, y=90)

        self.testLabel = Label(self.inputFrame, text='Qam', wraplength=245, anchor=W)
        self.testLabel.place(x=175, y=70)
        self.modChosen = StringVar()
        self.modChosen= ttk.Combobox(self.inputFrame, textvariable=self.modChosen, width=10)
        self.modChosen['values'] = ['QPSK', '16QAM', '64QAM', '256QAM']
        self.modChosen.place(x=150, y=90)

root = Tk()
Application(root)
if __name__ == "__main__":
    root.mainloop()