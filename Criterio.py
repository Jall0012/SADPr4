class Criterio:
    def __init__(self,Textopregunta,fil,col):
        self.pregunta = Textopregunta
        self.valoracion = 0
        self.fila = fil
        self.columna = col

    def valorar(self,valor):
        if valor >= -8 and valor <= 8:
            self.valoracion = valor

    def media(self):
        return self.valoracion