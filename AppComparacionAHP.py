import tkinter as tk
from tkinter import ttk, messagebox


class AppComparacionAHP:
    def __init__(self, root, diccionario_criterios):
        self.root = root
        self.root.title("Evaluación Multicriterio (AHP) - Múltiples Matrices")
        self.root.geometry("850x600")

        self.diccionario_criterios = diccionario_criterios
        self.respuestas_var = {}

        self.escala = [
            (9, -8, "red"), (8, -7, "red"), (7, -6, "red"), (6, -5, "red"),
            (5, -4, "red"), (4, -3, "red"), (3, -2, "red"), (2, -1, "red"),
            (1, 0, "black"),
            (2, 1, "purple"), (3, 2, "purple"), (4, 3, "purple"), (5, 4, "purple"),
            (6, 5, "purple"), (7, 6, "purple"), (8, 7, "purple"), (9, 8, "purple")
        ]

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.construir_interfaz()
        # Nota: El botón global ha sido eliminado de aquí

    def construir_interfaz(self):
        tab_instrucciones = tk.Frame(self.notebook, bg="#ffffff")
        self.notebook.add(tab_instrucciones, text="Instrucciones")

        # Título de las instrucciones
        lbl_titulo_inst = tk.Label(
            tab_instrucciones,
            text="Instrucciones de Evaluación Multicriterio (AHP)",
            font=("Arial", 16, "bold"),
            bg="#ffffff"
        )
        lbl_titulo_inst.pack(pady=20, padx=20, anchor="w")

        # Texto explicativo
        texto_inst = (
            "Cuestionario de valoración.\n\n"
            "Para cada pregunta, compare la importancia de los elementos mostrados a los lados:\n\n"
            "   Lado Izquierdo: El primer elemento tiene mas importancia que el segundo mencionado en la pregunta.\n"
            "   Lado Derecho: El segundo elemento tiene mas importancia que el primero mencionado en la pregunta.\n\n"
            "Significado de los números:\n"
            "   1 : Equal Importance\n"
            "   2 : Weak\n"
            "   3 : Moderate Importance\n"
            "   4 : Moderate Plus\n"
            "   5 : Strong Importance\n"
            "   6 : Strong Plus\n"
            "   7 : Very Strong or demon-strated importance\n"
            "   8 : Very, very strong\n"
            "   9 : Extreme importance\n"
        )

        lbl_texto_inst = tk.Label(
            tab_instrucciones,
            text=texto_inst,
            font=("Arial", 11),
            bg="#ffffff",
            justify="left"
        )
        lbl_texto_inst.pack(padx=20, pady=10, anchor="w")

        total_grupos = len(self.diccionario_criterios)

        # Usamos enumerate para saber el índice (i) de la pestaña actual
        for i, (nombre_grupo, lista_criterios) in enumerate(self.diccionario_criterios.items()):

            tab_frame = tk.Frame(self.notebook, bg="#ffffff")
            self.notebook.add(tab_frame, text=nombre_grupo)

            # Si es la última pestaña, anclamos el botón en la parte inferior
            if i == total_grupos - 1:
                btn_guardar = tk.Button(
                    tab_frame,
                    text="Guardar Valoraciones y Mostrar Resultados",
                    font=("Arial", 11, "bold"),
                    bg="#4CAF50",
                    fg="white",
                    padx=10,
                    pady=8,
                    command=self.procesar_respuestas
                )
                btn_guardar.pack(side="bottom", pady=15)

            # Canvas y Scrollbar
            canvas = tk.Canvas(tab_frame, borderwidth=0, background="#ffffff")
            scrollbar = tk.Scrollbar(tab_frame, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, background="#ffffff")

            scrollable_frame.bind(
                "<Configure>",
                lambda e, c=canvas: c.configure(scrollregion=c.bbox("all"))
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            # Empaquetamos el scroll y el canvas DESPUÉS del botón para que ocupen el resto del espacio
            scrollbar.pack(side="right", fill="y")
            canvas.pack(side="left", fill="both", expand=True)

            lbl_titulo = tk.Label(
                scrollable_frame,
                text=f"Comparación: {nombre_grupo}",
                font=("Arial", 16, "bold"),
                bg="#ffffff"
            )
            lbl_titulo.pack(pady=15, padx=20, anchor="w")

            for idx, crit in enumerate(lista_criterios):
                frame_criterio = tk.Frame(scrollable_frame, bg="#f9f9f9", bd=1, relief="solid", padx=10, pady=10)
                frame_criterio.pack(fill="x", expand=True, padx=20, pady=10)

                lbl_pregunta = tk.Label(
                    frame_criterio,
                    text=f"{idx + 1}. {crit.pregunta}",
                    font=("Arial", 11, "bold"),
                    bg="#f9f9f9",
                    justify="left"
                )
                lbl_pregunta.pack(anchor="w", pady=(0, 10))

                frame_escala = tk.Frame(frame_criterio, bg="#ffffff", bd=1, relief="solid")
                frame_escala.pack(fill="x", expand=True)

                lbl_elem_i = tk.Label(
                    frame_escala,
                    text=f"Elemento {crit.fila}",
                    font=("Arial", 10, "italic"),
                    bg="#ffffff",
                    width=15,
                    anchor="e"
                )
                lbl_elem_i.pack(side="left", padx=5)

                var_opcion = tk.IntVar(value=0)
                self.respuestas_var[crit] = var_opcion

                for texto_num, valor_num, color in self.escala:
                    sub_frame = tk.Frame(frame_escala, bg="#ffffff")
                    sub_frame.pack(side="left", expand=True, fill="both")

                    rb = tk.Radiobutton(
                        sub_frame,
                        text=str(texto_num),
                        value=valor_num,
                        variable=var_opcion,
                        fg=color,
                        selectcolor="#e6e6e6",
                        font=("Arial", 10, "bold"),
                        bg="#ffffff",
                        activebackground="#ffffff",
                        indicatoron=False,
                        bd=0,
                        padx=6,
                        pady=4
                    )
                    rb.pack(padx=1, pady=1)

                lbl_elem_j = tk.Label(
                    frame_escala,
                    text=f"Elemento {crit.columna}",
                    font=("Arial", 10, "italic"),
                    bg="#ffffff",
                    width=15,
                    anchor="w"
                )
                lbl_elem_j.pack(side="right", padx=5)

    def montarMatriz(self, criterios, elementos):
        mediaCriterio = [[0.0 for _ in range(elementos)] for _ in range(elementos)]

        for criterio in criterios:
            med = criterio.media()

            if med == 0:
                mediaCriterio[criterio.fila][criterio.columna] = 1.0
                mediaCriterio[criterio.columna][criterio.fila] = 1.0
            elif med > 0:
                mediaCriterio[criterio.columna][criterio.fila] = (med + 1)
                mediaCriterio[criterio.fila][criterio.columna] = (1.0 / (med + 1))
            elif med < 0:
                mediaCriterio[criterio.fila][criterio.columna] = ((-med) + 1)
                mediaCriterio[criterio.columna][criterio.fila] = (1.0 / ((-med) + 1))

        for i in range(elementos):
            mediaCriterio[i][i] = 1.0

        return mediaCriterio

    def procesar_respuestas(self):
        resumen = ""

        for nombre_grupo, lista_criterios in self.diccionario_criterios.items():
            resumen += f"=== {nombre_grupo} ===\n"

            for crit in lista_criterios:
                valor_seleccionado = self.respuestas_var[crit].get()
                crit.valorar(valor_seleccionado)

            max_index = 0
            for c in lista_criterios:
                if c.fila > max_index: max_index = c.fila
                if c.columna > max_index: max_index = c.columna

            num_elementos = max_index + 1

            matriz = self.montarMatriz(lista_criterios, num_elementos)

            resumen += "Matriz Resultante:\n"
            for fila in matriz:
                fila_formateada = "  ".join([f"{val:6.2f}" for val in fila])
                resumen += f"[{fila_formateada}]\n"
            resumen += "-" * 40 + "\n\n"

        ventana_resultados = tk.Toplevel(self.root)
        ventana_resultados.title("Resultados Guardados")
        ventana_resultados.geometry("500x400")

        frame_texto = tk.Frame(ventana_resultados)
        frame_texto.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = tk.Scrollbar(frame_texto)
        scrollbar.pack(side="right", fill="y")

        text_area = tk.Text(frame_texto, yscrollcommand=scrollbar.set, font=("Courier", 10))
        text_area.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text_area.yview)

        text_area.insert(tk.END, resumen)
        text_area.config(state="disabled")