#MONEDERO DIGITAL

#CREDENCIALES
useri = 'mike'
password = '0202'
import time
import os
saldo_total = 1000

#DEF
def usuario(a):
    return a.lower() == useri

def passw():
    for intentos in range (2,-1,-1):
        pin = input(f'{useri.capitalize()} por favor, ingrese su PIN: ')
        if pin == password:
            print('PIN confirmado\n')
            break
        else:
            print(f'PIN invalido, te quedan {intentos} intentos')
    else:
        print("Has agotado los 3 intentos. Acceso denegado")
        os._exit(0)


def menu():
    print (f'{useri.capitalize()}, Indique qué acción desea realizar:\n')
    print ('1. Saludar')
    print ('2. Hora del dia')
    print('3. Ver mi monedero')
    print('4. Salir')

def menu_monedero():
    print ('====MONEDERO====\n')
    print ('1. Ver saldo')
    print ('2. Retirar saldo')
    print ('3. Depositar saldo')
    print ('4. Volver al menu anterior')

def monedero():
     global saldo_total
     while True:
        menu_monedero()
        try:
            respuesta_dos = (int(input('Elija una opcion: ')))
            if respuesta_dos == 1:
                print(saldo_total)
            elif respuesta_dos == 2:
                print(f'Su saldo es: {saldo_total}\n')
                restasaldo = float(input('Ingrese el monto a retirar: '))
                if restasaldo <= saldo_total and restasaldo > 0 :
                    passw()
                    saldo_total = saldo_total - restasaldo
                    print(f'Retiro exitoso, su nuevo saldo será: {saldo_total}\n')
                    return
                else:
                    print('Monto no disponible, intente de nuevo\n')
            elif respuesta_dos == 3:
                nuevo_saldo = float(input('Ingrese la cantidad que desea depositar: '))
                if nuevo_saldo > 0:
                    saldo_total = saldo_total + nuevo_saldo 
                    print (f'Deposito exitoso!, su nuevo saldo es: {saldo_total}\n')
                    return
                else:
                    print('Monto no permitido\n')
            elif respuesta_dos == 4:
                break
            elif respuesta_dos > 4:
                print('Opción no válida, intente de nuevo\n')
        except:
            print('Entrada no reconocida, vuelva a intentarlo.')

#SOLICITUD DE USUARIO
print('====== Sistema de acceso seguro =====\n')
for intentos in range (2,-1,-1):
    a = input('Ingrese su usuario: ')
    if usuario(a):
        print('Usuario verificado')
        break
    else:
        print(f'Usuario incorrecto, te quedan {intentos} intentos')
else:
    print('Has agotado los 3 intentos. Acceso denegado')
    os._exit(0)

#SOLICITUD DE PIN
passw()
print('====Bienvenido====\n')

#MENU 
while True:
    menu()
    try:
        respuesta = int(input('Inserte un numero: '))
        if respuesta == 1:
            print(f'-Hola {useri.capitalize()}, espero que te encuentres muy bien!\n')
        elif respuesta == 2:
            print (f'-{useri.capitalize()}, La hora actual es: {time.strftime("%I:%M %p")}\n')
        elif respuesta == 3:    #MONEDERO
            monedero()
        elif respuesta == 4:
            print(f'-Hasta luego {useri.capitalize()}')
            break
        elif respuesta > 4:
            print('Error en la solicitud, seleccione una opcion valida')
    except:
        print('Error en la solicitud: Por favor seleccione un numero')