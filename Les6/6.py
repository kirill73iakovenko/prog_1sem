import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([])
y1 = np.array([])

def open_file():
    try:
        global text
        filepath = filedialog.askopenfilename()
        if filepath != "":
            with open(filepath, "r") as file:
                text = pd.read_csv(file)
    except KeyError:
        pass
def main():
    def approx(*args):
        global x1
        global y1
        x1 = np.array(list(text['PetalLengthCm']))
        y1 = np.array(list(text['PetalWidthCm']))
        k1, b1 = np.polyfit(x1, y1, 1)
        k.set(k1)
        b.set(b1)
        fig, ax = plt.subplots()
        x = np.array([1., 7.2])
        ax.plot(x, k1 * x + b1, "-r", linewidth=1, label='Линейная аппроксимация')
        ax.errorbar(x1, y1, yerr=0.01, xerr=0.001, color='b', linestyle='None', label='Экспериментальные точки')
        ax.set_xlabel("Длина лепестка, см")
        ax.set_ylabel("Ширина лепестка, см")
        ax.set_title("Зависимость ширины лепестков от их длины")
        ax.legend()
        plt.savefig('1.png')
    root = tk.Tk()
    root.geometry('300x200')

    tk.Button(root, text="Open the file", relief=tk.RAISED, bd=7, command=open_file).grid(row=0, column=0)
    k = tk.StringVar()
    b = tk.StringVar()
    tk.Button(root, text="Approximate data", relief=tk.RAISED, bd=7, command=approx).grid(row=0, column=1)
    tk.Label(root, text='MNC coefficients').grid(row=1, column=0)
    tk.Label(root, textvariable=k).grid(row=1, column=1)
    tk.Label(root, textvariable=b).grid(row=2, column=1)
    root.grid_columnconfigure(0, minsize=150)
    root.grid_columnconfigure(1, minsize=150)
    root.grid_rowconfigure(0, minsize=80)

    root.mainloop()

if __name__ == '__main__':
    main()
