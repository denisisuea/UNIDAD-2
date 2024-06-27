# SEMANA 4 TIPOS DE DATOS, IDENTIFICADORES
# ESTE PROGRAMA CALCULA EL ÁREA, PERÍMETRO Y DIÁMETRO DE UN CÍRCULO

# Importamos el valor de pi
from math import pi
print("Este programa calcula: ")
print("1.-Area de un circulo")
print("2.-Perímetro de un círculo")
print("3.-Diámetro de un círculo")
print("4.-Todos los cálculos anteriores")
print("Digite el número de cual de las cuatro opciones desea calcular")
opcion=int(input())

# Calcular Área del Circulo
def area_circulo():
    print("Esta opción del programa calcula el area de un círculo")
    print("Ingrese el valor del radio")
    radio = float(input())
    area_circulo = pi*(radio**2)
    print("El área del círculo es: ",round(area_circulo,2))

# Calcular Perímetro del Circulo
def perimetro_circulo():
    print("Esta opción del programa calcula el perimetro de un círculo")
    print("Ingrese el valor del radio")
    radio = float(input())
    perimetro = 2*radio*pi
    print("El valor del perímetro del círculo es: ",round(perimetro,2))

# Calcular el diámetro del Circulo
def diametro_circulo():
    print("Esta opción del programa calcula el Diámetro de un circulo")
    print("Ingrese el valor del radio")
    radio = float(input())
    diametro = radio/pi
    print("El valor del diametro: ",round(diametro,2))

# Todos los calculos anteriores
if opcion==1:
    area_circulo() # Llamamos a la función area_circulo

if opcion==2:
    perimetro_circulo() # Llamamos a la función perimetro_calculo

if opcion==3:
    diametro_circulo() # Llamamos a la función diametro_perimetro

if opcion==4:
    print("Esta opción del programa calcula: El área, el perímetro, y el diametro de un circulo ")
    area_circulo() 
    perimetro_circulo()
    diametro_circulo()   

# Realizado por: Dénisis Portilla    