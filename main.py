from Clases import *

listaMasc = []

opcion=int(input("OPCION 1- Agregar Mascota, 2-Modificar Mascota, 3-Borrar Mascota, 4-Saludar Dueño, 5-Ver Mascotas, 6- Salir: "))


while opcion != 6:

    if opcion == 1:

        opcionMascota=int(input("Desea agregar Perro(1), Gato(2), Pajaro(3) o Pez(4)?"))

        if opcionMascota == 1:

            nom = input("Escriba el nombre del perro: ")
            due = input("Escriba el nombre del dueño: ")


            verif = True

            for item in listaMasc:
                if item.nombre == nom:
                    print("No se pudo agregar, nombre duplicado")
                    verif = False

            if verif == True:

                Perrito = Perro(nom, due)
                listaMasc.append(Perrito)
                print("Se agrego satisfactoriamente")

        elif opcionMascota == 2:

            nom = input("Escriba el nombre del gato: ")
            due = input("Escriba el nombre del dueño: ")

            verif = True

            for item in listaMasc:
                if item.nombre == nom:
                    print("No se pudo agregar, nombre duplicado")
                    verif = False

            if verif == True:
                Gatito = Gato(nom, due)
                listaMasc.append(Gatito)
                print("Se agrego satisfactoriamente")


        elif opcionMascota == 3:


            nom = input("Escriba el nombre del pajaro: ")
            due = input("Escriba el nombre del dueño: ")
            cant = input("El pajaro es cantor?")

            if cant == "si":

                canto = input("Cual es su canto?: ")

                Pajaro = Pajarito(nom,due,canto)

            elif cant == "no":

                Pajaro = Pajarito(nom,due)

            verif = True

            for item in listaMasc:
                if item.nombre == nom:
                    print("No se pudo agregar, nombre duplicado")
                    verif = False

            if verif == True:

                listaMasc.append(Pajaro)
                print("Se agrego satisfactoriamente")

        elif opcionMascota == 4:

            nom = input("Escriba el nombre del pez: ")
            due = input("Escriba el nombre del dueño: ")

            verif = True

            for item in listaMasc:
                if item.nombre == nom:
                    print("No se pudo agregar, nombre duplicado")
                    verif = False

            if verif == True:
                Pescadito = Pez(nom, due)
                listaMasc.append(Pescadito)
                print("Se agrego satisfactoriamente")


    elif opcion == 2:

        for item in listaMasc:

            print(item.nombre + "\n")

        nom = input("Escriba el nombre de la mascota que quiere modificar")

        for item in listaMasc:

            if item.nombre == nom:

                nomM = input("Escriba el nuevo nombre: ")
                dueM = input("Escriba el nuevo dueño: ")

                if item.__class__.__name__ == 'Pajarito':

                    canM = input("Es cantor?: (si/no)")


                    verif = True

                    for item2 in listaMasc:
                        if item2.nombre == nomM and item.nombre != nomM:
                            print("No se pudo agregar, nombre duplicado")

                            verif = False

                    if verif == True:
                        item.nombre = nomM
                        item.dueño = dueM
                        if canM == "si":

                            cantoM = input("Cual es su nuevo canto?")

                            item.saludo = cantoM

                        print("Se agrego satisfactoriamente")

                else:

                        verif = True

                        for item2 in listaMasc:
                            if item2.nombre == nomM:

                                print("No se pudo agregar, nombre duplicado")

                                verif = False

                        if verif == True:

                            item.nombre = nomM
                            item.dueño = dueM

                            print("Se agrego satisfactoriamente")


    elif opcion == 3:
        break


    elif opcion ==4:

        break

    elif opcion == 5:

        for item in listaMasc:

            print(item.nombre +"   " + item.dueño +"   " + item.saludo + "\n")


    opcion=int(input("OPCION 1- Agregar Mascota, 2-Modificar Mascota, 3-Borrar Mascota, 4-Saludar Dueño, 5-Ver Mascotas, 6- Salir: "))






