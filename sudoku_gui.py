import tkinter as tk

main_window=tk.Tk()
main_window.title("Sudoku")
main_window.geometry("500x500")

title=tk.Label(main_window, text="Sudoku",font=('Arial',20))
title.pack(padx=15,pady=15)

main_window.mainloop()