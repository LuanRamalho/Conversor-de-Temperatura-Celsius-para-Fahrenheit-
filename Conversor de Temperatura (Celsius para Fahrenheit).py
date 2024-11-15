import tkinter as tk
from tkinter import ttk

def converter_temperatura():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = celsius * 9/5 + 32
        kelvin = celsius + 273.15
        label_fahrenheit['text'] = f"Fahrenheit: {fahrenheit:.2f}°F"
        label_kelvin['text'] = f"Kelvin: {kelvin:.2f}K"
    except ValueError:
        label_fahrenheit['text'] = "Fahrenheit: Entrada inválida!"
        label_kelvin['text'] = "Kelvin: Entrada inválida!"

# Criando a janela principal
janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry("400x300")
janela.configure(bg="#f0f8ff")

# Título
titulo = tk.Label(janela, text="Conversor de Temperatura", font=("Arial", 16, "bold"), bg="#4682b4", fg="white", pady=10)
titulo.pack(fill=tk.X)

# Caixa de entrada para Celsius
frame_celsius = tk.Frame(janela, bg="#f0f8ff")
frame_celsius.pack(pady=20)
label_celsius = tk.Label(frame_celsius, text="Graus Celsius (°C):", font=("Arial", 12), bg="#f0f8ff")
label_celsius.pack(side=tk.LEFT, padx=5)
entry_celsius = ttk.Entry(frame_celsius, font=("Arial", 12))
entry_celsius.pack(side=tk.LEFT, padx=5)

# Botão para converter
btn_converter = tk.Button(janela, text="Converter", command=converter_temperatura, font=("Arial", 12, "bold"), bg="indigo", fg="white")
btn_converter.pack(pady=10)

# Resultado Fahrenheit
label_fahrenheit = tk.Label(janela, text="Fahrenheit: --°F", font=("Arial", 12), bg="#f0f8ff", fg="#4682b4")
label_fahrenheit.pack()

# Resultado Kelvin
label_kelvin = tk.Label(janela, text="Kelvin: --K", font=("Arial", 12), bg="#f0f8ff", fg="#4682b4")
label_kelvin.pack()

# Loop principal da janela
janela.mainloop()
