import tkinter as tk

def calc(op):
    a = float(entry1.get())
    b = float(entry2.get())
    
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = "Помилка" if b == 0 else a / b
    
    label_result.config(text="Результат: " + str(result))

window = tk.Tk()
window.title("Калькулятор")

tk.Label(window, text="Перше число:").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Друге число:").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

tk.Button(window, text="+", command=lambda: calc("+")).grid(row=2, column=0)
tk.Button(window, text="-", command=lambda: calc("-")).grid(row=2, column=1)
tk.Button(window, text="*", command=lambda: calc("*")).grid(row=3, column=0)
tk.Button(window, text="/", command=lambda: calc("/")).grid(row=3, column=1)

label_result = tk.Label(window, text="")
label_result.grid(row=4, column=0, columnspan=2)

window.mainloop()