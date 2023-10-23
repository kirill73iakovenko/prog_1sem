import tkinter as tk


def clear(m, h):
    m.set('')
    h.set('')

def main():
    def calc(*args):
        try:
            m= int(mass.get())
            h = int(height.get()) / 100
            imt.set(int(m / (h ** 2)))
        except ValueError:
            pass
        if int(imt.get()) < 16:
            level.set('Underweight (Severe thinness)')
        elif int(imt.get()) >= 16 and int(imt.get()) < 16.9:
            level.set('Underweight (Moderate thinness)')
        elif int(imt.get()) >= 17 and int(imt.get()) < 18.5:
            level.set('Underweight (Mild thinness)')
        elif int(imt.get()) >= 18.5 and int(imt.get()) < 25:
            level.set('Normal range')
        elif int(imt.get()) >= 25 and int(imt.get()) < 30:
            level.set('Overweight (Pre-obese)')
        elif int(imt.get()) >= 30 and int(imt.get()) < 35:
            level.set('Obese (Class I)')
        elif int(imt.get()) >= 35 and int(imt.get()) < 40:
            level.set('Obese (Class II)')
        else:
            level.set('Obese (Class III)')
    root = tk.Tk()
    root.geometry('700x300')
    photo = tk.PhotoImage(file='Obesity_&_BMI.png')
    root.iconphoto(False, photo)
    root.title('Body mass index')
    mass = tk.StringVar()
    mass_entry = tk.Entry(root, textvariable = mass)
    height = tk.StringVar()
    height_entry = tk.Entry(root, textvariable = height)
    label1 = tk.Label(root, text='Enter the mass', font='15', bg='#b5f7b7')
    label2 = tk.Label(root, text='Enter the height', font='15', bg='#b5f7b7')
    imt = tk.StringVar()
    button1 = tk.Button(root, text='Result', font='15', bg='#ed2828', relief=tk.RAISED, bd=7, command=lambda : calc(mass, height))
    label3 = tk.Label(root, textvariable=imt, font='15')
    button2 = tk.Button(root, text='Clear the input field', font='15', bg='#ed2828', relief=tk.RAISED, bd=7, command=lambda : clear(mass, height))
    label4 = tk.Label(root, text='Your BMI', font='15', bg='#2491b3')
    level = tk.StringVar()
    label5 = tk.Label(root, textvariable=level, font='15')

    mass_entry.grid(row=0, column=0, stick='nswe')
    height_entry.grid(row=1, column=0, stick='nswe')
    label1.grid(row=0, column=1, stick='nswe')
    label2.grid(row=1, column=1, stick='nswe')
    button1.grid(row=2, column=0, stick='nswe')
    button2.grid(row=2, column=1, stick='nswe')
    label3.grid(row=3, column=0, stick='nswe')
    label4.grid(row=3, column=1, stick='nswe')
    label5.grid(row=4, column=0, stick='nswe')

    root.grid_rowconfigure(0, minsize=50)
    root.grid_rowconfigure(1, minsize=50)
    root.grid_rowconfigure(2, minsize=50)
    root.grid_rowconfigure(3, minsize=50)

    root.grid_columnconfigure(0, minsize=350)
    root.grid_columnconfigure(1, minsize=350)
    root.grid_columnconfigure(3, minsize=350)

    root.mainloop()

if __name__ == '__main__':
    main()

