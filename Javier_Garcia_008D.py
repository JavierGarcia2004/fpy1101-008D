import csv
import os
import time
import random
os.system('cls')
pedidos = []
def numeroPedido():
    return random.randint(1,1000)

# registrar al cliente 
def registrarPedido():

    nombre = input("Ingresar el nombre del cliente: ")
    apellido = input("Ingresar el apellido del cliente: ")
    direccion = input("Ingresar la direccion del cliente: ")
    sector = input("Igresar el sector o comuna donde vive: ")
    sacos_5 = int(input("Ingresar la cantidad de sacos de 5kg: "))
    sacos_10 = int(input("Ingresar la cantidad de sacos de 10 kg: "))
    sacos_20 = int(input("Ingresar la cantidad de sacos de 20kg que desea llevar: "))
    pedido = {'numeroPedido':numeroPedido,
              'nombre':nombre,
              'apellido':apellido,
              'direccion':direccion,
              'sector':sector,
              'sacos de 5kg':sacos_5,
              'sacos de 10 kg':sacos_10,
              'sacos de 20 kg':sacos_20
            }
      
    pedidos.append(pedido)
    guardarPedidoCsv(pedido)
    print(f"pedido{numeroPedido}registrado exitosamente")
    # guardado de pedido
def guardarPedidoCsv(pedido):
    with open('pedidos.csv','a',newline='')as file:
        writer = csv.DictWriter(fieldnames=pedido.keys())
        if file.tell()==0:
            writer.writeheader()
        writer.writerow(pedido)
        
#listar pedido        
def listarPedido():
    if not pedidos:
        print("No hay pedidos registrados.")
    else:
        for pedido in pedidos:
            print(pedido)

#Hoja de ruta              
def imprimirHojaRuta():
    if not pedidos:
        print("No hay pedidos para imprimir.")
    else:
        with open('imprimirHojaRuta.txt','w') as file:
            for pedido in pedidos:
                file.write(str(pedido)+"\n")
                print("hoja de ruta impresa en imprimirHojaRuta.txt")
def menu():
    
    #menu del clientw
    
    while True:
        print("Menu")
        print("1-Registrar pedido.")
        print("2-Listar todo los pedidos.")
        print("3-Imprimir hoja de ruta.")
        print("4-Salir del programa")
        # opciones del cliente
        opcion = int(input("Ingrese su opcion:"))
       
        if opcion  ==1:
            print("****Registrar usuario****")
            registrarPedido()
            
        elif opcion ==2:
            print("****listar pedido****")
            listarPedido()
            
        elif opcion ==3:
            print("****Hoja de ruta****")
            imprimirHojaRuta()
            
        elif opcion ==4:
            print("Saliendo del programa....")
            break
        
        else:print("Ingrese una opcion valida porfavor intente denuevo....")
menu()
