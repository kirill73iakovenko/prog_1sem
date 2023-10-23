import tkinter as tk




def main():
    def com_color(*args):
        col = color.get()
        part1 = int(col[1:3], 16)
        part2 = int(col[3:5], 16)
        part3 = int(col[5:7], 16)
        result.set('#' + str(hex(255-part1)[2:])+str(hex(255-part2)[2:])+str(hex(255-part3)[2:]))

    root = tk.Tk()
    root.geometry('300x200')
    color = tk.StringVar()
    tk.Entry(root, textvariable=color).grid(row=0, column=0)
    tk.Label(root, text='Enter a color', font=15).grid(row=0, column=1)
    result = tk.StringVar()
    tk.Button(root, text='Find a complementary color', relief=tk.RAISED, bd=7, command=com_color).grid(row=1, columnspan=2)
    tk.Label(root, textvariable=result).grid(row=2, columnspan=2)


    root.grid_columnconfigure(1, minsize=150)
    root.mainloop()

if __name__ == '__main__':
    main()
