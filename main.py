import tkinter as tk

from clases.filosofo import filosofo

if __name__=="__main__":
  

window = tk.Tk()
window.title("La cena de los filósofos")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()