import tkinter as tk

main_window=tk.Tk()
main_window.title("Sudoku")
main_window.geometry("500x500")

title=tk.Label(main_window, text="Sudoku",font=('Arial',20))
title.pack(padx=15,pady=15)

frame=tk.Frame(main_window)
frame.pack()
id_entry = tk.Entry(frame)
id_entry.grid(row=1,column=0)

for x in range(3):
    for y in range(3):
        pass
main_window.mainloop()