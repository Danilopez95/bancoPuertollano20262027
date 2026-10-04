from cliente import cargarCliente
from logs import Log
import os

log = Log()

def menu():

    while True:

        print("1) Cargar datos cliente")
        print("2) Consultar cuenta y deposito")
        print("3) Listar clientes cargados")
        print("4) Salir")

        opt = input("Introduce la opción deseada: ")

        if opt == "1":
            cargarCliente("movimientos")

        elif opt == "2":
            cliente = cargarCliente("guardado")
            if cliente is not None:
                log.escribir("INFO", f"CONSULTA DATOS CLIENTE CON NÚMERO: {cliente.numero}")
            print(f"Cliente: {cliente.numero}")
            print(f"Saldo cuenta: {cliente.cuenta.saldo} €")
            print(f"Saldo depósito: {cliente.deposito.saldo} €")

        elif opt == "3":
            print("Clientes cargados:\n")

            archivos = os.listdir("datosClientes")

            for archivo in archivos:
                numero_cliente = os.path.splitext(archivo)[0]
                print(f"- {numero_cliente}")

        elif opt == "4":
            log.escribir(
                "INFO",
                "FIN EJECUCIÓN"
            )
            print("Hasta pronto")
            break

        else:
            log.escribir(
                "WARNING",
                "SE HA INTRODUCIDO UNA OPCION EN EL MENÚ NO RECONOCIDA"
            )
            print("No se ha seleccionado ninguna opción correcta")