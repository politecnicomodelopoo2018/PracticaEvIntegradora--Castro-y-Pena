class Mascota(object):

    nombre = None
    duenio=None
    saludo = None

    def __init__(self, nom, due, sal):

        self.nombre=nom
        self.duenio=due
        self.saludo=sal

    def modificarMascota(self, nom, due, sal):

        self.nombre = nom
        self.duenio = due
        self.saludo=sal














