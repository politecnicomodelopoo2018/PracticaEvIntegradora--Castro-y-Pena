from mascota import Mascota

class Pajaro(Mascota):

    cantante = None


    def __init__(self,nom,due,sal,cant):

        if cant == 0:
            self.nombre = nom
            self.duenio = due
            self.saludo = sal
            self.cantante = cant

        if cant == 1:
            self.nombre = nom
            self.duenio = due
            self.saludo = sal
            self.cantante = cant

    def modificarPajaro(self, nom, due, sal, cant):

        if cant == 0:

            self.nombre = nom
            self.duenio = due
            self.saludo= sal
            self.cantante = cant

        if cant == 1:

            self.nombre = nom
            self.duenio = due
            self.saludo = sal
            self.cantante = cant


