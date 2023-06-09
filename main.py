import variables as vb
import clases as cl
from funciones import *
import os 



numero = None
reiniciar = False

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while True:
    if numero == None:
        try:
            numero = float(input(vb.mensaje1))
            inicio_calculadora(numero)
            print("\n")
        except:
            numero = None
            print("ERROR!!!!")


    try:
        print("Acumulado: ")
        mostrar_acumulado()
        print("\n")
        operacion = int(float(input(vb.mensaje2)))
        # print(operacion)
        if operacion == 6:
            break
        elif operacion == 5:
            reiniciar = True
            if reiniciar == True:
                numero = None
                reiniciar_calculadora()
                reiniciar = False
                continue



        print("\n")
        numero2 = float(input(vb.mensaje3))
        if operacion == 4:
            if numero2 == 0:
                print("Error!!!")
                continue

        operacion_calculadora(operacion, numero2)

    except:
        print("ERROR!!!!")
        continue
