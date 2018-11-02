from veterinario import Veterinario
from mascota import  Mascota
from pajarito import Pajaro

Vete = Veterinario()

opcion=int(input("OPCION 1- Agregar Mascota, 2-Modificar Mascota, 3-Borrar Mascota, 4-Saludar Dueño, 5- Salir"))


while opcion != 5:

    if opcion == 1:

        opcionMascota=int(input("Desea agregar Perro(1), Gato(2) o Pajaro(3)?"))

        if opcionMascota == 1:

            nombre = input("Que nombre tiene el perro?")
            duenio = input("Que nombre tiene el dueño?")

            perro = Mascota(nombre, duenio, "guau")

            Vete.agregarMascotasALista(perro)

        if opcionMascota == 2:

            nombre = input("Que nombre tiene el gato?")
            duenio = input("Que nombre tiene el dueño?")

            gato = Mascota(nombre, duenio, "miau")

            Vete.agregarMascotasALista(gato)

        if opcionMascota == 3:

            nombre = input("Que nombre tiene el pajaro?")
            duenio = input("Que nombre tiene el dueño?")

            cantante = int(input("Es cantante? SI = 1 , NO = 0"))

            if cantante == 1:

                saludo = input("Cual es su saludo?")

                pajarito = Pajaro(nombre,duenio,saludo,cantante)

                Vete.agregarMascotasALista(pajarito)

            elif cantante == 0:

                pajarito = Pajaro(nombre,duenio,"pio",cantante)

                Vete.agregarMascotasALista(pajarito)

    elif opcion == 2:

        for item in Vete.listaMascotas:

            print(item.nombre)

        nombreModificar = input("Ingrese el nombre de la mascota que desea modificar")

        # for item in Vete.listaMascotas:
        #
        #     if item.nombre == nombreModificar:





                # if item.saludo == "pio" or (item.saludo!="guau" and item.saludo!= "miau"):
                #     nombreModificado = input("Nombre nuevo mascota: ")
                #     duenioModificado = input("Nombre nuevo Dueño: ")
                #     esCantante = int(input("Es cantante?"))

                        # if esCantante == 1:
                        #
                        #     saludoModificado = input("Nuevo saludo:  ")
                        #
                        # elif esCantante == 0:
                        #
                        #     saludoModificado = "pio"

    elif opcion == 3:

        for item in Vete.listaMascotas:
            print(item.nombre)

        nombreBorrar = input("Ingrese el nombre de la mascota que desea eliminar")

        for item in Vete.listaMascotas:

            if item.nombre == nombreBorrar:

                Vete.listaMascotas.remove(item)

    elif opcion ==4:

        nombre = input("Que nombre tiene el pajaro?")
        duenio = input("Que nombre tiene el dueño?")

        print(Vete.saludarDuenio(duenio,nombre))

    opcion = int(input("OPCION 1- Agregar Mascota, 2-Modificar Mascota, 3-Borrar Mascota, 4-Saludar Dueño, 5- Salir"))







