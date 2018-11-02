
class Veterinario(object):

    listaMascotas = []

    def agregarMascotasALista(self,objeto):

        self.listaMascotas.append(objeto)

    def borrarMascota(self,nom):

        for item in self.listaMascotas:

            if item.nombre == nom:

                self.listaMascotas.remove(item)


    def cositasRicas(self, objeto):

        for item in self.listaMascotas:

            if item.nombre == objeto.nombre:

                if item.cantante:

                    item.nombre = objeto.nombre
                    item.duenio = objeto.duenio
                    item.saludo= objeto.saludo
                    item.cantante = objeto.cantante

                else:

                    item.nombre = objeto.nombre
                    item.duenio = objeto.duenio
                    item.saludo = objeto.saludo

    def saludarDuenio(self, nomDue, nomMas):

        for item in self.listaMascotas:

            if item.nombre == nomMas and item.duenio == nomDue:

                return item.saludo


            elif item.nombre == nomMas and item.duenio != nomDue:

                if (item.saludo == "pio" and item.cantante == 0)or item.cantante == 1:

                    return ""

                return item.saludo.upper()+"!"
