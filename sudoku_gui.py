import tkinter as tk

main_window = tk.Tk()
main_window.title("Sudoku")
main_window.geometry("800x800")

support_frame = tk.Frame(main_window, height=600, width=600, bg='green', padx=10, pady=10)
support_frame.pack()
# Center support_frame both horizontally and vertically
support_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title = tk.Label(support_frame, text="Sudoku", font=('Arial', 20))
title.pack(padx=15, pady=15)

sudoku_frame = tk.Frame(support_frame, bg="red")
sudoku_frame.pack()

entries = []

for x in range(9):
    entries.append([])
    for y in range(9):
        entries[x].append(tk.Entry(sudoku_frame, justify="center", width=2, font=('Arial', 24)))
        entries[x][y].grid(row=x, column=y)

check_button=tk.Button(support_frame,text="Check",width=7, height=2)
check_button.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

restart_icon=tk.PhotoImage(file="restart_icon.png")
restart_icon=restart_icon.subsample(15,15)

restart_button=tk.Button(support_frame,image=restart_icon,width=60, height=35)
restart_button.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

save_button=tk.Button(support_frame,text="Save",width=7, height=2)
save_button.pack(padx=10,pady=10,side=tk.LEFT, fill=tk.BOTH, expand=True)

main_window.mainloop()