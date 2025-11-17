import tkinter as tk

def show_name():
    name = entry.get()
    label_result.config(text="Привіт, " + name + "!")

window = tk.Tk()
window.title("Введення імені")

label = tk.Label(window, text="Введіть ім'я:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Відправити", command=show_name)
button.pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()