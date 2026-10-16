# ============================================================
# Sistema de Control de Gastos Personales
# Paradigma: ORIENTADO A OBJETOS (POO)
# Archivo: main.py
#
# Menu interactivo que INSTANCIA objetos y usa los metodos
# de las clases Gasto y GestorGastos.
# ============================================================

from gasto import Gasto
from gestor_gastos import GestorGastos


def pedir_monto(mensaje):
    """Solicita un monto valido por consola."""
    while True:
        entrada = input(mensaje).strip()
        try:
            monto = float(entrada)
            if monto <= 0:
                print("El monto debe ser mayor que cero.")
                continue
            return monto
        except ValueError:
            print("Entrada invalida. Ingrese un numero.")


def mostrar_menu():
    """Muestra el menu de opciones."""
    print("\n" + "=" * 45)
    print("   SISTEMA DE CONTROL DE GASTOS PERSONALES")
    print("        (Paradigma Orientado a Objetos)")
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
    # Instanciacion del gestor (objeto principal)
    gestor = GestorGastos()

    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            # Funcionalidad 1: registrar gasto (se instancia un Gasto)
            print("\n--- REGISTRAR GASTO ---")
            concepto = input("Concepto (descripcion): ").strip()
            if concepto == "":
                print("El concepto no puede estar vacio.")
                continue
            monto = pedir_monto("Monto ($): ")
            categoria = input(
                "Categoria (Alimentacion/Transporte/Servicios/Entretenimiento): "
            ).strip()
            if categoria == "":
                categoria = "Sin categoria"

            nuevo_gasto = Gasto(concepto, monto, categoria)  # instanciacion
            gestor.agregar_gasto(nuevo_gasto)                # composicion
            print("Gasto registrado correctamente.")

        elif opcion == "2":
            # Funcionalidad 2: mostrar listado
            print("\n--- LISTADO DE GASTOS ---")
            lista = gestor.get_gastos()
            if gestor.cantidad() == 0:
                print("No hay gastos registrados.")
                continue
            print(f"{'#':<4}{'CONCEPTO':<25}{'CATEGORIA':<20}{'MONTO':>12}")
            print("-" * 61)
            for i in range(len(lista)):
                g = lista[i]
                print(f"{i + 1:<4}{g.get_concepto():<25}{g.get_categoria():<20}{g.get_monto():>12.2f}")
            print("-" * 61)
            print(f"Total de registros: {gestor.cantidad()}")

        elif opcion == "3":
            # Funcionalidad 3: total acumulado
            print("\n--- GASTO TOTAL ACUMULADO ---")
            if gestor.cantidad() == 0:
                print("No hay gastos registrados.")
                continue
            print(f"Gasto total acumulado: ${gestor.calcular_total():.2f}")

        elif opcion == "4":
            # Funcionalidad 4: gasto de mayor valor
            print("\n--- GASTO DE MAYOR VALOR ---")
            mayor = gestor.obtener_mayor()
            if mayor is None:
                print("No hay gastos registrados.")
                continue
            print(mayor)  # usa el metodo __str__ de la clase Gasto

        elif opcion == "5":
            # Funcionalidad 5: filtrar por monto
            print("\n--- GASTOS MAYORES A UN MONTO ---")
            if gestor.cantidad() == 0:
                print("No hay gastos registrados.")
                continue
            umbral = pedir_monto("Mostrar gastos mayores a ($): ")
            resultados = gestor.filtrar_por_monto(umbral)
            if len(resultados) == 0:
                print(f"No hay gastos mayores a ${umbral:.2f}.")
            else:
                for g in resultados:
                    print(f"- {g}")
                print(f"Cantidad de coincidencias: {len(resultados)}")

        elif opcion == "6":
            # Funcionalidad 6: buscar por concepto
            print("\n--- BUSCAR GASTO POR CONCEPTO ---")
            if gestor.cantidad() == 0:
                print("No hay gastos registrados.")
                continue
            palabra = input("Palabra clave a buscar: ").strip()
            if palabra == "":
                print("Debe ingresar una palabra clave.")
                continue
            resultados = gestor.buscar_por_concepto(palabra)
            if len(resultados) == 0:
                print("No se encontraron coincidencias.")
            else:
                for g in resultados:
                    print(f"- {g}")
                print(f"Coincidencias encontradas: {len(resultados)}")

        elif opcion == "0":
            print("\nSaliendo del sistema. Hasta pronto.")
        else:
            print("Opcion invalida. Intente de nuevo.")


if __name__ == "__main__":
    main()
