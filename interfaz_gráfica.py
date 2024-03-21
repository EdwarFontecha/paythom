# Edwar Arley Fontecha Chuiquiza
import tkinter as tk

class Persona:
    total_personas = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    total_estudiantes = 0
    
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1
        
    def imprimir_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

class Profesor:
    def __init__(self, nombre, edad, departamento):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
        
    def presentar(self):
        print(f"Soy el profesor {self.nombre}, tengo {self.edad} años y trabajo en el departamento de {self.departamento}.")

class EstudianteProfesor(Estudiante, Profesor):
    def __init__(self, nombre, edad, carrera, departamento):
        Estudiante.__init__(self, nombre, edad, carrera)
        Profesor.__init__(self, nombre, edad, departamento)
        
    def info_completa(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Departamento: {self.departamento}")

def saludar_persona():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()
    departamento = entry_departamento.get()

    persona = EstudianteProfesor(nombre, edad, carrera, departamento)
    persona.saludar()

root = tk.Tk()
root.title("Saludo de Persona")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_nombre = tk.Label(frame, text="Nombre:")
label_nombre.grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=0, column=1)

label_edad = tk.Label(frame, text="Edad:")
label_edad.grid(row=1, column=0, sticky="e")
entry_edad = tk.Entry(frame)
entry_edad.grid(row=1, column=1)

label_carrera = tk.Label(frame, text="Carrera:")
label_carrera.grid(row=2, column=0, sticky="e")
entry_carrera = tk.Entry(frame)
entry_carrera.grid(row=2, column=1)

label_departamento = tk.Label(frame, text="Departamento:")
label_departamento.grid(row=3, column=0, sticky="e")
entry_departamento = tk.Entry(frame)
entry_departamento.grid(row=3, column=1)

button_saludar = tk.Button(frame, text="Saludar", command=saludar_persona)
button_saludar.grid(row=4, columnspan=2)

root.mainloop()

