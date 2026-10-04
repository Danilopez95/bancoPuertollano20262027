from cliente import cargarCliente
from logs import Log

log = Log()

def menu():

    while True:

        print("1) Cargar Datos Cliente")
        print("2) Consultar cuenta Deposito")
        print("3) Salir")

        opt = input("Introduce la opción deseada: ")

        if opt == "1":
            cargarCliente("movimientos")

        elif opt == "2":
            cliente = cargarCliente("guardado")

            if cliente is not None:
                log.escribir(
                    "INFO",
                    f"CONSULTA DATOS CLIENTE CON NÚMERO: {cliente.numero}"
                )

                print(f"Cliente: {cliente.numero}")
                print(f"Saldo cuenta: {cliente.cuenta.saldo} €")
                print(f"Saldo depósito: {cliente.deposito.saldo} €")
                print(f"Saldo total: {cliente.getSaldoTotal()} €")

            else:
                log.escribir(
                    "ERROR",
                    "INTENTO DE CONSULTAR UN CLIENTE QUE NO HA SIDO CARGADO"
                )
                print("No hay ningún cliente cargado")

        elif opt == "3":
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