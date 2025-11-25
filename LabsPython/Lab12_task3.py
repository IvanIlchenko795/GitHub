import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Помилка")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

#ГОЛОВНЕ ВІКНО
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

#ПОЛЕ ВВЕДЕННЯ
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, justify="right")
entry.pack(fill="x", padx=10, pady=10, ipady=8)

#КНОПКИ
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', 'C', '+'],
    ['=']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), height=2, width=5)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

#ЗАПУСК
root.mainloop()