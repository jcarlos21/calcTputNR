from tkinter import *
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

        # Barra de Menu

        menubar = Menu(root)
        file1 = Menu(root, tearoff=False)
        file1.add_command(label="Exit", command=self.exitLogin)
        menubar.add_cascade(label="File", menu=file1)
        self.root.config(menu=menubar)

        # Parâmetros de Entrada

        self.inputFrame = LabelFrame(self.root, text='Input Parameters', width=390, height=200, font=('TkDefaultFont', 10, "bold"))
        self.inputFrame.grid(row=0, column=0, padx=25, pady=15)

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
        self.caChosen = StringVar()
        self.caChoose= ttk.Combobox(self.inputFrame, textvariable=self.caChosen, width=10)
        self.caChoose['values'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.caChoose.place(x=270, y=30)

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

        self.testLabel = Label(self.inputFrame, text='MIMO', wraplength=245, anchor=W)
        self.testLabel.place(x=290, y=70)
        self.mimoChosen = StringVar()
        self.mimoChoose= ttk.Combobox(self.inputFrame, textvariable=self.mimoChosen, width=10)
        self.mimoChoose['values'] = ['2x2', '4x4', '8x8']
        self.mimoChoose.place(x=270, y=90)

        # Botão cálcular

        self.botaoCalcular = Button(self.inputFrame, text="Calculate", borderwidth=3, cursor="hand2")
        self.botaoCalcular['command'] = self.calculateRate
        self.botaoCalcular.place(x=162, y=130)

        # Parâmetros de Saída:

        self.ouputFrame = LabelFrame(self.root, text='Output Parameters', width=390, height=90, font=('TkDefaultFont', 10, "bold"))
        self.ouputFrame.grid(row=1, column=0, padx=25, pady=0)

        # Mensagens com os resultados

        self.mensagemTAXA = Label(self.ouputFrame, text='Maximum Transmission Rate', wraplength=295, anchor=W)
        self.mensagemTAXA.place(x=10, y=7)
        self.l1 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=7)
        self.l1.place(x=175, y=7)
        self.mensagemMbps = Label(self.ouputFrame, text='Mbps', wraplength=200, anchor=W)
        self.mensagemMbps.place(x=235, y=7)

        self.mensagemTAXA2 = Label(self.ouputFrame, text='Minimum Transmission Rate', wraplength=295, anchor=W)
        self.mensagemTAXA2.place(x=10, y=35)
        self.l2 = Label(self.ouputFrame, borderwidth=2, relief="groove", width=7)
        self.l2.place(x=175, y=35)
        self.mensagemMbps2 = Label(self.ouputFrame, text='Mbps', wraplength=200, anchor=W)
        self.mensagemMbps2.place(x=235, y=35)
    
    def calculateRate(self):

        calculateNR = ResourceNR()
        calculateNR.fr = self.frChosen.get()
        calculateNR.bw = self.bwChosen.get()
        calculateNR.ca = self.caChosen.get()
        calculateNR.scs = self.scsChosen.get()
        calculateNR.modulation = self.modChosen.get()
        calculateNR.mimo = self.mimoChosen.get()

        maxRateNR, minRateNR = calculateNR.calcTputNR()

        self.l1['text'] = maxRateNR
        self.l2['text'] = minRateNR
    
    def exitLogin(self):
        result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            self.root.destroy() 

root = Tk()
Application(root)
if __name__ == "__main__":
    root.mainloop()