from tkinter import *

class Ventana (Tk):
  def __init__(self, titulo, color='misty rose', geometria = '550x250'):
    Tk.__init__(self)
    self.title(titulo)
    self.geometry(geometria)
    self.configure(background=color)

