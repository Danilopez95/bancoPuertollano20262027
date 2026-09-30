from menu import menu
from logs import Log

log = Log()

if __name__ == '__main__':
    try:
        menu()
    except BaseException as e:
        log.escribir(
            "ERROR",
            f"Se ha producido un error de aplicacion {e}"
        )
        print(f"Se ha producido un error de aplicacion {e}")
