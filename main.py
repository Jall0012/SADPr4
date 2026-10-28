# This is a sample Python script.
import tkinter as tk  # ✅ Importación correcta del módulo principal
from tkinter import messagebox

from AppComparacionAHP import AppComparacionAHP
from Criterio import Criterio


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    Matrizcriterios = [
        Criterio("¿Como de importantes son la cantidad de datos moviles respecto a la canidad de minutos de  llamada?", 0, 1),
        Criterio("¿Como de importantes son la cantidad de datos moviles respecto al precio mensual?", 0, 2),
        Criterio("¿Como de importantes son la cantidad de datos moviles respecto a la permanencia?", 0, 3),
        Criterio("¿Como de importantes son la cantidad de minutos de llamada respecto al precio mensual?", 1, 2),
        Criterio("¿Como de importantes son la cantidad de minutos de llamada respecto a la permanencia", 1, 3),
        Criterio("¿Como de importantes son la cantidad de precio mensual respecto a la permanencia?", 2, 3)
    ]

    MatrizDatos = [
        Criterio("¿Como de superiores son 16 GB de datos moviles respecto a 50 GB?",0,1),
        Criterio("¿Como de superiores son 16 GB de datos moviles respecto a 31 GB?", 0, 2),
        Criterio("¿Como de superiores son 16 GB de datos moviles respecto a 31 GB?", 0, 3),
        Criterio("¿Como de superiores son 50 GB de datos moviles respecto a 31 GB?", 1, 2),
        Criterio("¿Como de superiores son 50 GB de datos moviles respecto a 31 GB?", 1, 3),
        Criterio("¿Como de superiores son 31 GB de datos moviles respecto a 31 GB?", 2, 3)
    ]

    MatrizPrecio = [
        Criterio("¿Como de superiores son 25,99€ de coste respecto a 29,90€?", 0, 1),
        Criterio("¿Como de superiores son 25,99€ de coste moviles respecto a 17,90€?", 0, 2),
        Criterio("¿Como de superiores son 25,99€ de coste moviles respecto a 19,90€?", 0, 3),
        Criterio("¿Como de superiores son 29,90€ de coste moviles respecto a 17,90€", 1, 2),
        Criterio("¿Como de superiores son 29,90€ de coste moviles respecto a 19,90€?", 1, 3),
        Criterio("¿Como de superiores son 17,90€ de coste moviles respecto a 19,90€?", 2, 3)
    ]

    MatrizPermanencia = [
        Criterio("¿Como de superiores son 6 meses de permanencia respecto a 0 meses?", 0, 1),
        Criterio("¿Como de superiores son 6 meses de permanencia respecto a 6 meses", 0, 2),
        Criterio("¿Como de superiores son 6 meses de permanencia respecto a 12 meses?", 0, 3),
        Criterio("¿Como de superiores son 0 meses de permanencia respecto a 6 meses", 1, 2),
        Criterio("¿Como de superiores son 0 meses de permanencia respecto a 12 meses?", 1, 3),
        Criterio("¿Como de superiores son 6 meses de permanencia respecto a 12 meses?", 2, 3)
    ]

    MatrizTiempoLlamada = [
        Criterio("¿Como de superiores son 200 minutos de llamada respecto a 90 minutos?", 0, 1),
        Criterio("¿Como de superiores son 200 minutos de llamada respecto a 100 minutos?", 0, 2),
        Criterio("¿Como de superiores son 200 minutos de llamada respecto a minutos ilimitados?", 0, 3),
        Criterio("¿Como de superiores son 90 minutos de llamada respecto a 100 minutos", 1, 2),
        Criterio("¿Como de superiores son 90 minutos de llamada respecto a minutos ilimitados?", 1, 3),
        Criterio("¿Como de superiores son 100 minutos de llamada respecto a minutos ilimitados?", 2, 3)
    ]

    ListaMatrices = {"Comparación criterios":Matrizcriterios,"Comparación de datos":MatrizDatos,"Comparación de precios":MatrizPrecio,"Comparación de permanencia":MatrizPermanencia,"Comparación de tiempo de llamada":MatrizTiempoLlamada}
    root = tk.Tk()
    app = AppComparacionAHP(root, ListaMatrices)
    root.mainloop()