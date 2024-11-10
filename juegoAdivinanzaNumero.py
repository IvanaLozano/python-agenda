import random

def juegoAdivinanza():
    #generar un numero del 1 al 100
    numeroSecreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    
    print("Bienvenido al juego de adivinanza de numero")
    print("Debes adivinar un numero del 1 al 100")
    print("Intenta adivinarlo")
    
    while not adivinado:
        #solicitar un numero
        adivinanza = input("Introdusca un numero del 1 al 100: ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos +=1

            if adivinanza < numeroSecreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numeroSecreto:
                print(f"El numero secreto es menor a {adivinanza}")

            else:
                print(f"Felicidades has ganado. El numero {adivinanza} es el numero secreto y lo has logrado en {intentos}")
    
    else:
        print("Por favor introduzca un numero valido entre el 1 al 100")



juegoAdivinanza()

