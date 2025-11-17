import tkinter as tk

def convert():
    amount = float(entry.get())
    currency = var.get()
    if currency == 1:
        result = amount * 42  # умовний курс USD
    else:
        result = amount * 45  # умовний курс EUR
    label_result.config(text=f"{result:.2f} грн")

window = tk.Tk()
window.title("Конвертер валюти")

label = tk.Label(window, text="Введіть суму:")
label.pack()

entry = tk.Entry(window)
entry.pack()

var = tk.IntVar()

radio1 = tk.Radiobutton(window, text="USD → UAH", variable=var, value=1)
radio1.pack()
radio2 = tk.Radiobutton(window, text="EUR → UAH", variable=var, value=2)
radio2.pack()

button = tk.Button(window, text="Конвертувати", command=convert)
button.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()