import os
import time

pikachu_roll = 4500
otaku_roll = 5000
pulpo_roll = 5200
anguila_roll = 4800
cantidad1 = 0
cantidad2 = 0
cantidad3 = 0 
cantidad4 = 0
total= 0
descuento =10/100

os.system("cls")

print("Porfavor ingresar su nombre:")
nombre = input()
os.system("cls")
print("!! Bienvenido",nombre,"!!")
print("1-hacer mi pedido")
print("2-salir")
menu_salir = int(input("ingrese una opcion:"))
os.system("cls")
if menu_salir==1:
    
    os.system("cls")
    print("___________MENU____________")
    print("1-Pikachu Roll:$4500")
    print("2-Otaku Roll:$5000")
    print("3-Pulpo Venenoso Roll:$5200")
    print("4-Anguila Electrica Roll")
    opc = int(input("ingrese una opcion:"))
elif menu_salir==2:
    print("hasta la proxima",nombre)

if menu_salir ==1:
    print("ingrese la cantidad")
    cantidad1 = int(input())
    if opc ==2:
        print("ingrese la cantidad")
        cantidad2 = int(input())
        if opc ==3:
            print("ingrese la cantidad:")
            cantidad3 = int(input())
            if opc ==4:
                print("ingrese la cantidad")
                cantidad4 = int(input())







