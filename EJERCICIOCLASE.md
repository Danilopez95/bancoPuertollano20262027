# Práctica en parejas: Git + Banco Puertollano 2027

## Objetivo

Partiendo del proyecto **Banco Puertollano 2027**, trabajaréis en
parejas simulando un flujo de trabajo real con **Git y GitHub**.

Durante la práctica tendréis que corregir errores existentes y añadir
nuevas funcionalidades utilizando ramas, commits y *Pull Requests*.

**Duración:** 2 horas\
**Modalidad:** parejas

------------------------------------------------------------------------

## 1. Preparación del repositorio

Para esta práctica trabajaremos mediante **fork**.

1.  Uno de los miembros de la pareja realizará un **Fork** del
    repositorio proporcionado por el profesor.
2.  Añadirá al compañero como colaborador de ese fork.
3.  Ambos alumnos clonarán **el mismo fork** en sus equipos.
4.  Se comprobará que el proyecto funciona antes de realizar
    modificaciones.
5.  En el fork existirán dos ramas permanentes:

``` text
main
develop
```

La rama `main` representa la versión estable del proyecto.

La rama `develop` será la rama donde se integrará el trabajo realizado
durante la práctica.

> **IMPORTANTE:** No se trabajará directamente ni en `main` ni en
> `develop`.

------------------------------------------------------------------------

## 2. Flujo de trabajo

Cada tarea deberá realizarse en una rama independiente.

El flujo será:

``` text
main
  │
  └── develop
        │
        ├── feature/...
        ├── bugfix/...
        ├── feature/...
        └── bugfix/...
```

Cuando una tarea esté terminada:

``` text
rama feature/bugfix
        ↓
Pull Request
        ↓
develop
```

Cuando todas las tareas estén integradas y el programa funcione
correctamente:

``` text
develop
    ↓
Pull Request
    ↓
main
```

El compañero deberá **revisar el Pull Request antes de fusionarlo**.

------------------------------------------------------------------------

## 3. Normas de trabajo

-   En una rama **solo puede trabajar un alumno**.
-   Los dos miembros de la pareja pueden trabajar simultáneamente, pero
    siempre en ramas diferentes.
-   Está prohibido programar directamente sobre `main`.
-   Está prohibido programar directamente sobre `develop`.
-   Antes de crear una rama nueva se debe actualizar `develop`.
-   Cada tarea tendrá su propia rama.
-   Cada tarea debe terminar con un **Pull Request hacia `develop`**.
-   El compañero revisará el código antes de hacer el *merge*.
-   Los commits deben tener mensajes descriptivos.
-   No se deben subir `.venv`, logs ni ficheros generados por la
    aplicación.
-   El proyecto deberá seguir funcionando después de cada integración.

------------------------------------------------------------------------

## 4. Nomenclatura de ramas

Utilizaremos dos tipos de ramas.

### Nuevas funcionalidades

``` text
feature/numero-descripcion
```

Ejemplos:

``` text
feature/03-mostrar-resumen
feature/07-contador-movimientos
```

### Corrección de errores

``` text
bugfix/numero-descripcion
```

Ejemplos:

``` text
bugfix/01-cliente-inexistente
bugfix/05-linea-corrupta
```

No se utilizarán espacios, tildes ni mayúsculas en los nombres de las
ramas.

------------------------------------------------------------------------

# 5. Tareas

Las tareas se repartirán entre los dos miembros de la pareja. Cada
alumno será responsable de sus propias ramas.

## Tarea 1 --- BUGFIX: Consulta de cliente inexistente

**Rama:**

``` text
bugfix/01-cliente-inexistente
```

Actualmente, al consultar un cliente que no ha sido cargado previamente,
el programa puede intentar acceder a sus datos aunque el cliente sea
`None`.

Corregir el problema para que:

-   La aplicación no termine inesperadamente.
-   Se muestre un mensaje adecuado.
-   Se registre el intento en el log con nivel `ERROR`.

------------------------------------------------------------------------

## Tarea 2 --- FEATURE: Registrar la carga de clientes

**Rama:**

``` text
feature/02-log-carga-cliente
```

Añadir trazabilidad al proceso de carga de movimientos.

El log deberá registrar:

-   Inicio de la carga del cliente.
-   Cliente cargado correctamente.
-   Fichero de movimientos inexistente.

Utilizar correctamente los niveles `INFO` y `ERROR`.

------------------------------------------------------------------------

## Tarea 3 --- FEATURE: Mostrar resumen después de cargar

**Rama:**

``` text
feature/03-resumen-carga
```

Después de procesar correctamente el fichero de movimientos, mostrar:

``` text
Cliente: 334433
Saldo cuenta: XXXX €
Saldo depósito: XXXX €
```

La información debe obtenerse del objeto `Cliente`.

------------------------------------------------------------------------

## Tarea 4 --- BUGFIX: Validar el tipo de log

**Rama:**

``` text
bugfix/04-validar-tipo-log
```

La clase `Log` permite actualmente escribir cualquier tipo de mensaje.

Modificarla para aceptar únicamente:

``` text
INFO
WARNING
ERROR
```

Si se recibe otro tipo, deberá registrarse como `INFO`.

La aplicación no deberá detenerse.

------------------------------------------------------------------------

## Tarea 5 --- BUGFIX: Movimiento con cantidad incorrecta

**Rama:**

``` text
bugfix/05-cantidad-incorrecta
```

Un fichero podría contener una línea como:

``` text
hola;Ingreso;Cuenta;
```

Actualmente la conversión a `float` produciría un error.

Modificar el programa para que:

-   Ignore ese movimiento.
-   Continúe procesando el resto del fichero.
-   Registre un `ERROR` indicando la línea problemática.

------------------------------------------------------------------------

## Tarea 6 --- BUGFIX: Operación o destino desconocido

**Rama:**

``` text
bugfix/06-movimiento-desconocido
```

Controlar movimientos como:

``` text
200;Transferencia;Cuenta;
```

o:

``` text
200;Ingreso;Tarjeta;
```

Si la operación o el destino no están reconocidos:

-   El movimiento no se realizará.
-   El programa continuará.
-   Se añadirá un `WARNING` al log.

------------------------------------------------------------------------

## Tarea 7 --- FEATURE: Contador de movimientos

**Rama:**

``` text
feature/07-contador-movimientos
```

Durante la lectura del fichero se deberá contar cuántos movimientos
válidos se han procesado.

Al finalizar se mostrará:

``` text
Movimientos procesados: 50
```

También deberá registrarse esta información en el log.

------------------------------------------------------------------------

## Tarea 8 --- FEATURE: Consultar saldo total

**Rama:**

``` text
feature/08-saldo-total
```

Añadir a la clase `Cliente` un método:

``` python
def getSaldoTotal(self):
```

que devuelva la suma de:

``` text
saldo cuenta + saldo depósito
```

En la opción de consulta deberá mostrarse también:

``` text
Saldo total: XXXX €
```

------------------------------------------------------------------------

## Tarea 9 --- FEATURE: Nueva opción "Listado de clientes"

**Rama:**

``` text
feature/09-listado-clientes
```

Añadir una nueva opción al menú:

``` text
3) Listar clientes cargados
```

La opción deberá mostrar los números de los clientes que tienen datos
guardados en la carpeta:

``` text
datosClientes/
```

Ejemplo:

``` text
Clientes cargados:

- 334433
- 443344
```

La opción `Salir` pasará a ser la opción **4**.

------------------------------------------------------------------------

## Tarea 10 --- FEATURE: Mejorar el fichero de datos del cliente

**Rama:**

``` text
feature/10-formato-datos-cliente
```

Modificar el fichero generado en `datosClientes` para que cada dato
aparezca en una línea:

``` text
334433
1250.0
3500.0
```

Adaptar también la lectura del fichero para que la opción de consulta
siga funcionando correctamente.

> Esta tarea afecta tanto a la escritura como a la lectura. Comprobad
> que un cliente puede guardarse y recuperarse correctamente.

------------------------------------------------------------------------


# 8. Entrega

La pareja entregará la **URL del fork**.

En GitHub deberá poder comprobarse:

-   Rama `main`.
-   Rama `develop`.
-   Ramas utilizadas durante el desarrollo.
-   Commits realizados por ambos alumnos.
-   Pull Requests realizados.
-   Revisión de Pull Requests por el compañero.
-   Uso correcto de ramas `feature` y `bugfix`.
-   Proyecto final funcionando en `main`.

------------------------------------------------------------------------

## Resultado esperado

El objetivo no es únicamente que el programa funcione.

Al finalizar la práctica debéis haber utilizado un flujo de trabajo
similar al empleado en un proyecto colaborativo:

``` text
Tarea
  ↓
Rama feature/bugfix
  ↓
Commits
  ↓
Push
  ↓
Pull Request
  ↓
Revisión del compañero
  ↓
develop
  ↓
Pruebas finales
  ↓
main
```
