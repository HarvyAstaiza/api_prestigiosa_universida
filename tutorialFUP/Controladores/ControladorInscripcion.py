from tutorialFUP.Modelos.Inscripcion import Inscripcion
from tutorialFUP.Repositorios.RepositorioInscripcion import RepositorioInscripcion
"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInscripcion():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioInscripcion = RepositorioInscripcion()
        print("Creando ControladorInscripcion")

    def index(self):
        print("Listar todas las Inscripciones")
        return self.repositorioInscripcion.findAll()

    def create(self, laInscripcion):
        print("Crear un Inscripcion")
        nuevaInscripcion = Inscripcion(laInscripcion)
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show(self, id):
        print("Mostrando un Inscripcion con id ", id)
        elEstudiante = Inscripcion(self.repositorioInscripcion.findById(id))
        return elEstudiante.__dict__

    def update(self, id, laInscripcion):
        print("Actualizando Inscripcion con id ", id)
        inscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcionActual.nombre = laInscripcion["nombre"]
        inscripcionActual.semestre = laInscripcion["semestre"]
        inscripcionActual.nota_final = laInscripcion["nota_final"]
        return self.repositorioInscripcion.save(inscripcionActual)

    def delete(self, id):
        print("Eliminando departamento con id ", id)
        return self.repositorioInscripcion.delete(id)