class Mascota (object):

    nombre = ""
    dueño = None
    saludo = ""

    def saludar(self, persona):

        if self.dueño == persona:

            return self.saludo

        return self.saludo.upper() + "!"

    def __init__(self, nom, due):

        self.nombre = nom
        self.dueño = due

class Perro(Mascota):

    saludo = "guau"

class Gato(Mascota):

    saludo = "miau"

class Pajarito(Mascota):

    saludo = ""

    def __init__(self, nom, due, saludo = "pio"):

        Mascota.__init__(self, nom, due)

        self.saludo = saludo

    def saludar(self, persona):

        if self.dueño == persona:

            return self.saludo

        return ""


class Pez(Mascota):

    saludo = ""
    vidas = 10

    def alimentarme(self):

        self.vidas += 1


    def saludar(self, persona):

        if self.dueño == persona:

            self.vidas -= 1

        self.vidas = 0
