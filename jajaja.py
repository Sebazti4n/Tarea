from inspect import Traceback
import os
import random
import time
from unicodedata import name
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
from datetime import date
from datetime import datetime


prueba = "Descripcion prueba"

ocupado = [0, 1, 2, 3, 4, 5]
disponible = [6, 7]

folio = {
    "Microsoft":[
            22445,
            f"{prueba}",
            "Matutino",
            "04:00:00",
            0
        ],
    "Apple":[
            77788,
            f"{prueba}",
            "Matutino",
            "09:00:00",
            1
        ],
    "Sony":[
            99999,
            f"{prueba}",
            "Matutino",
            "00:12:00",
            2
        ],
    "Reels":[
            88834,
            f"{prueba}",
            "Matutino",
            "12:00:00",
            3
        ],
    "Tkinter":[
            99034,
            f"{prueba}",
            "Matutino",
            "00:45:00",
            4
        ],
    "Sisco":[
            34256,
            f"{prueba}",
            "Matutino",
            "20:23:00",
            5
        ]
    }

desc = ["nada","nada","nada","nada","nada","nada",]
clavesys = [2244553335,3333377788,9444449999,8555558834,9555559034,3425555556]

numeri = 0
neimi = ""
descripi = ""
horarioki = ""
hor_registri = 0
console = Console()
class estaili:
    def estilillo1():
        table = Table(title="Reservaciones ya hechas",show_header=True)
        table.add_column("No.")
        table.add_column("Descripcion")
        table.add_column("Nombre de la empresa")
        table.add_column("Horario")
        table.add_column("Fecha de registro")
        table.add_column("Sala")
        for n in folio:
            folios = folio[n][0]
            descrichon = folio[n][1]
            horariok = folio[n][2]
            registrado = folio[n][3]
            sala = folio[n][4]
            x = str(folios)
            y = str(descrichon)
            z = str(horariok)
            r = str(registrado)
            o = str(sala)
            
            table.add_row(x,n,y,z,r,o)
        console.print(table) 

def pt2edit():
    os.system("cls")
    nombrexdf = input("Nombre de evento: ")
    nuev = input("Nuevo nombre del evento: ")
    fo = folio[nombrexdf][0]
    fo1 = folio[nombrexdf][1]
    fo2 = folio[nombrexdf][2]
    fo3 = folio[nombrexdf][3]
    fo4 = folio[nombrexdf][4]

    folio[nuev] = [fo,fo1,fo2,fo3,fo4]
    del folio[nombrexdf]
    



def edit():
    os.system("cls")
    table = Table(title="Reservaciones ya hechas",show_header=True)
    table.add_column("No.")
    table.add_column("Descripcion")
    table.add_column("Nombre de la empresa")
    table.add_column("Horario")
    table.add_column("Fecha de registro")
    table.add_column("Sala")
    for n in folio:
        folios = folio[n][0]
        descrichon = folio[n][1]
        horariok = folio[n][2]
        registrado = folio[n][3]
        sala = folio[n][4]
        x = str(folios)
        y = str(descrichon)
        z = str(horariok)
        r = str(registrado)
        o = str(sala)
        
        table.add_row(x,n,y,z,r,o)
    console.print(table)
    print("")
    clav = input("Ingresa tu clave de usuario registrado: ")
    pt2edit()

    

def regis():
    name = input("Ingresa nombre: ")
    clavexd = random.randint(1111111111,9999999999)
    print("")
    print(f"Se te genero una clave de usuario registrado: {clavexd}")
    console.print(":warning: Guarda bien tu clave por favor")
    clavesys.append(clavexd)

def cuery():
    estaili.estilillo1()

def menu():
        os.system("cls")
        print("################################\n#      Menu Principal          #\n################################")
        print("")
        print("1 - Registrar reservacion de sala")
        print("2 - Editar nombre de evento")
        print("3 - Consultar reservaciones")
        print("4 - Registrarte")
        print("5 - Salir")
        print("")

        name = int(input("-> "))

        if name == 1:
            os.system("cls")
            reserva()
            menu()
        elif name == 2:
            edit()
            time.sleep(3)
            menu()
        elif name == 3:
            print(folio)
            time.sleep(5)
            cuery()
            time.sleep(15)
            menu()
        elif name == 4:
            os.system("cls")
            regis()
            time.sleep(10)
            menu()
        elif name == 5:
            os.system("cls")
            print("")
            print('Saliendo...')
            time.sleep(2)
            os.system("cls")
        else:
            menu()

def reserva():
    #try:
        print("##################################\n#      Ingresa tus clave         #\n##################################")
        print("")
        print("Ingresa tu clave de usuario registrado para poder continuar")
        clave = int(input("Clave -> "))

        if clave in clavesys:
            print("")
            os.system("cls")
            print("Clave encontrada")
            print("")
            os.system("cls")

            nombre = input("Nombre de el evento: ")
            desciption = input("Para que se usara la sala? ")

            horario = input("Matutino, Vespertino o Nocturno? (M, V, N): ")
            if horario == "M":
                horario = "Matutino"
            elif horario == "V":
                horario = "Vespertino"
            elif horario == "N":
                horario = "Nocturno"      
            else:
                os.system("cls")
                print("Creo que te tendre que devolver por listo...")
                time.sleep(5)
                reserva()
            try:        
                lugar = int(input(f"En que sala?,\nSalas disponibles: {disponible}"))
            except ValueError as r:
                print("Pon una sala valida") 
            num = random.randint(11111,99999)
            today = date.today()
            folio[nombre] = [num,desciption,horario,today,lugar]

            print("")

            print(f"Se hizo la reservacion a nombre de {nombre} para {desciption}, en horario {horario}")
            print(f"No. folio: {num}")

        else:
            print("")
            os.system("cls")
            print("Esta clave no existe, crea una")
            time.sleep(5)
        

"""     except:
        os.syatem("cls")
        print("Clave no registrada...") """

def apepe():
    try:
        menu()

    except ValueError as e:
        print("")
        print("Algo a salido mal...")
        print(e)
        time.sleep(5)
        os.system("cls")
        menu()
    except TypeError as t:
        print("")
        print("Algo a salido mal...")
        print(t)
        time.sleep(5)
        os.system("cls")
        menu()

a = 3

if a == 3:
    apepe()