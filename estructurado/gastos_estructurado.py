# ============================================================
# Sistema de Control de Gastos Personales
# Paradigma: ESTRUCTURADO
# Archivo: gastos_estructurado.py
#
# Caracteristicas del paradigma aplicadas:
#   - Variables globales y locales
#   - Estructuras condicionales (if / else)
#   - Ciclos (while, for)
#   - Funciones independientes con paso de parametros
#   - Menu secuencial interactivo en consola
#   - Estructuras de datos nativas (lista de diccionarios)
#   - SIN clases personalizadas ni librerias de alto nivel
# ============================================================

# ---------- VARIABLE GLOBAL ----------
# Lista global que almacena todos los gastos del usuario.
# Cada gasto es un diccionario con las claves: concepto, monto, categoria.
gastos = []


# ---------- FUNCIONES INDEPENDIENTES ----------

def registrar_gasto(lista_gastos):
    """Solicita los datos de un gasto y lo agrega a la lista."""
    print("\n--- REGISTRAR GASTO ---")
    concepto = input("Concepto (descripcion): ").strip()

    if concepto == "":
        print("El concepto no puede estar vacio.")
        return

    # Validacion del monto con un ciclo while
    monto = 0.0
    while True:
        entrada = input("Monto ($): ").strip()
        try:
            monto = float(entrada)
            if monto <= 0:
                print("El monto debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Entrada invalida. Ingrese un numero.")

    categoria = input(
        "Categoria (Alimentacion/Transporte/Servicios/Entretenimiento): "
    ).strip()
    if categoria == "":
        categoria = "Sin categoria"

    # Se crea el diccionario y se anade a la lista nativa
    nuevo_gasto = {
        "concepto": concepto,
        "monto": monto,
        "categoria": categoria
    }
    lista_gastos.append(nuevo_gasto)
    print("Gasto registrado correctamente.")


def mostrar_gastos(lista_gastos):
    """Presenta la totalidad de gastos registrados de forma organizada."""
    print("\n--- LISTADO DE GASTOS ---")
    if len(lista_gastos) == 0:
        print("No hay gastos registrados.")
        return

    # Encabezado de la tabla
    print(f"{'#':<4}{'CONCEPTO':<25}{'CATEGORIA':<20}{'MONTO':>12}")
    print("-" * 61)

    # Ciclo for para recorrer la coleccion
    for i in range(len(lista_gastos)):
        g = lista_gastos[i]
        print(f"{i + 1:<4}{g['concepto']:<25}{g['categoria']:<20}{g['monto']:>12.2f}")
    print("-" * 61)
    print(f"Total de registros: {len(lista_gastos)}")


def calcular_total(lista_gastos):
    """Suma el valor numerico de todos los egresos registrados."""
    print("\n--- GASTO TOTAL ACUMULADO ---")
    if len(lista_gastos) == 0:
        print("No hay gastos registrados.")
        return

    # Variable local acumuladora y ciclo for explicito
    total = 0.0
    for g in lista_gastos:
        total = total + g["monto"]

    print(f"Gasto total acumulado: ${total:.2f}")


def mostrar_gasto_mayor(lista_gastos):
    """Identifica y despliega el registro con el monto mas elevado."""
    print("\n--- GASTO DE MAYOR VALOR ---")
    if len(lista_gastos) == 0:
        print("No hay gastos registrados.")
        return

    # Se asume el primero como mayor y se compara con el resto
    mayor = lista_gastos[0]
    for g in lista_gastos:
        if g["monto"] > mayor["monto"]:
            mayor = g

    print(f"Concepto : {mayor['concepto']}")
    print(f"Categoria: {mayor['categoria']}")
    print(f"Monto    : ${mayor['monto']:.2f}")


def filtrar_por_monto(lista_gastos):
    """Lista los gastos cuyo monto supere un umbral ingresado."""
    print("\n--- GASTOS MAYORES A UN MONTO ---")
    if len(lista_gastos) == 0:
        print("No hay gastos registrados.")
        return

    umbral = 0.0
    while True:
        entrada = input("Mostrar gastos mayores a ($): ").strip()
        try:
            umbral = float(entrada)
            break
        except ValueError:
            print("Entrada invalida. Ingrese un numero.")

    # Copia local del subconjunto filtrado
    resultados = []
    for g in lista_gastos:
        if g["monto"] > umbral:
            resultados.append(g)

    if len(resultados) == 0:
        print(f"No hay gastos mayores a ${umbral:.2f}.")
    else:
        for g in resultados:
            print(f"- {g['concepto']} ({g['categoria']}): ${g['monto']:.2f}")
        print(f"Cantidad de coincidencias: {len(resultados)}")


def buscar_por_concepto(lista_gastos):
    """Localiza coincidencias por subcadena en el concepto."""
    print("\n--- BUSCAR GASTO POR CONCEPTO ---")
    if len(lista_gastos) == 0:
        print("No hay gastos registrados.")
        return

    palabra = input("Palabra clave a buscar: ").strip().lower()
    if palabra == "":
        print("Debe ingresar una palabra clave.")
        return

    # Variables locales para el resultado
    encontrados = 0
    for g in lista_gastos:
        if palabra in g["concepto"].lower():
            print(f"- {g['concepto']} ({g['categoria']}): ${g['monto']:.2f}")
            encontrados = encontrados + 1

    if encontrados == 0:
        print("No se encontraron coincidencias.")
    else:
        print(f"Coincidencias encontradas: {encontrados}")


def mostrar_menu():
    """Despliega el menu secuencial interactivo."""
    print("\n" + "=" * 45)
    print("   SISTEMA DE CONTROL DE GASTOS PERSONALES")
    print("=" * 45)
    print("1. Registrar gasto")
    print("2. Mostrar listado de gastos")
    print("3. Calcular gasto total acumulado")
    print("4. Mostrar el gasto de mayor valor")
    print("5. Mostrar gastos mayores a un monto")
    print("6. Buscar gasto por concepto")
    print("0. Salir")
    print("=" * 45)


def main():
    """Funcion principal: controla el flujo con un ciclo while."""
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_gasto(gastos)
        elif opcion == "2":
            mostrar_gastos(gastos)
        elif opcion == "3":
            calcular_total(gastos)
        elif opcion == "4":
            mostrar_gasto_mayor(gastos)
        elif opcion == "5":
            filtrar_por_monto(gastos)
        elif opcion == "6":
            buscar_por_concepto(gastos)
        elif opcion == "0":
            print("\nSaliendo del sistema. Hasta pronto.")
        else:
            print("Opcion invalida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
