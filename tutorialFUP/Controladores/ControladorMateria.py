from tutorialFUP.Modelos.Materia import Materia
from tutorialFUP.Repositorios.RepositorioDepartamento import RepositorioDepartamento
from tutorialFUP.Repositorios.RepositorioMateria import RepositorioMateria
from tutorialFUP.Modelos.Departamento import Departamento

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMateria():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """

    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()
        print("Creando ControladorMateria")

    def index(self):
        print("Listar todas las Materias")
        return self.repositorioMateria.findAll()

    def create(self, laMateria):
        print("Crear una Materia")
        nuevaMateria = Materia(laMateria)
        return self.repositorioMateria.save(nuevaMateria)

    def show(self, id):
        print("Mostrando una Materia con id ", id)
        lamateria = Materia(self.repositorioMateria.findById(id))
        return lamateria.__dict__

    def update(self, id, laMateria):
        print("Actualizando Materia con id ", id)
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = laMateria["nombre"]
        materiaActual.creditos = laMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        print("Elimiando estudiante con id ", id)
        return self.repositorioMateria.delete(id)

    def asignarDepartamento(self, id, id_departamento):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.repositorioMateria.save(materiaActual)
