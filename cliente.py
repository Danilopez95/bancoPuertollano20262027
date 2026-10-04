from models import Cliente
from logs import Log

log = Log()

def cargarCliente(tipo):
    while True:
        num = input("Introduce el número de cliente: ")

        if len(num) != 6 or not num.isdigit():
            print("El formato introducido no es correcto")
            continue

        if tipo == "movimientos":
            return leerFichero(num)

        elif tipo == "guardado":
            return cargarClienteGuardado(num)


def leerFichero(numCliente):

    cliente = Cliente(numCliente)
    log.escribir(
        "INFO",
        f"INICIO DE CARGA DEL CLIENTE: {numCliente}"
    )

    try:
        with open(f"ficherosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()

            while linea:

                datos = linea.strip().split(";")

                try:
                    cantidad = float(datos[0])
                except ValueError:
                    log.escribir(
                        "ERROR",
                        f"CANTIDAD INCORRECTA EN LA LINEA: {linea.strip()}"
                    )
                    linea = f.readline()
                    continue

                operacion = datos[1]
                destino = datos[2]

                if destino == "Cuenta" and operacion == "Ingreso":
                    cliente.cuenta.ingresar(cantidad)

                elif destino == "Cuenta" and operacion == "Retirada":
                    cliente.cuenta.retirar(cantidad)

                elif destino == "Deposito" and operacion == "Ingreso":
                    cliente.deposito.ingresar(cantidad)

                elif destino == "Deposito" and operacion == "Retirada":
                    cliente.deposito.retirar(cantidad)

                else:
                    log.escribir(
                        "WARNING",
                        f"MOVIMIENTO DESCONOCIDO: {linea.strip()}"
                    )

                linea = f.readline()

        # Guardamos el estado final del cliente
        cliente.guardar()

        print(f"Cliente: {cliente.numero}")
        print(f"Saldo cuenta: {cliente.cuenta.saldo} €")
        print(f"Saldo depósito: {cliente.deposito.saldo} €")
        log.escribir(
            "INFO",
            f"CLIENTE CARGADO CORRECTAMENTE: {numCliente}"
        )

        print("Datos del cliente cargados correctamente")

        return cliente

    except FileNotFoundError:
        log.escribir(
            "ERROR",
            f"FICHERO DE MOVIMIENTOS INEXISTENTE PARA EL CLIENTE: {numCliente}"
        )
        print("El usuario no tiene ninguna cuenta con el banco")
        return None


def cargarClienteGuardado(numCliente):

    try:
        with open(f"datosClientes/{numCliente}.txt", "r") as f:

            linea = f.readline()
            datos = linea.split(";")

            cliente = Cliente(datos[0])

            cliente.cuenta.saldo = float(datos[1])
            cliente.deposito.saldo = float(datos[2])

            return cliente

    except FileNotFoundError:
        print("Primero tienes que cargar los datos de este cliente")
        return None