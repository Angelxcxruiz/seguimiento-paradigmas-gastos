# ============================================================
# Sistema de Control de Gastos Personales
# Paradigma: ORIENTADO A OBJETOS (POO)
# Archivo: gestor_gastos.py
#
# Clase que administra la coleccion de objetos Gasto.
# Aplica COMPOSICION: un GestorGastos TIENE una lista de Gastos.
# Implementa las 6 funcionalidades requeridas.
# ============================================================

from gasto import Gasto


class GestorGastos:
    """Administra una coleccion de objetos Gasto."""

    def __init__(self):
        # Composicion: el gestor contiene objetos de la clase Gasto
        self.__gastos = []

    # ------------- Funcionalidad 1: Registrar gasto -------------

    def agregar_gasto(self, gasto):
        """Agrega un objeto Gasto a la coleccion."""
        if not isinstance(gasto, Gasto):
            raise TypeError("Solo se pueden agregar objetos de tipo Gasto.")
        self.__gastos.append(gasto)

    def get_gastos(self):
        """Devuelve la coleccion completa de gastos."""
        return self.__gastos

    def cantidad(self):
        """Devuelve cuantos gastos hay registrados."""
        return len(self.__gastos)

    # ----------- Funcionalidad 3: Calcular total acumulado ------

    def calcular_total(self):
        """Suma el monto de todos los gastos registrados."""
        total = 0.0
        for gasto in self.__gastos:
            total += gasto.get_monto()
        return total

    # ----------- Funcionalidad 4: Gasto de mayor valor ----------

    def obtener_mayor(self):
        """Devuelve el objeto Gasto con el monto mas alto."""
        if self.cantidad() == 0:
            return None
        mayor = self.__gastos[0]
        for gasto in self.__gastos:
            if gasto.get_monto() > mayor.get_monto():
                mayor = gasto
        return mayor

    # -------- Funcionalidad 5: Gastos mayores a un monto --------

    def filtrar_por_monto(self, umbral):
        """Devuelve una lista con los gastos mayores al umbral."""
        resultado = []
        for gasto in self.__gastos:
            if gasto.get_monto() > umbral:
                resultado.append(gasto)
        return resultado

    # ----------- Funcionalidad 6: Buscar por concepto -----------

    def buscar_por_concepto(self, palabra):
        """Devuelve los gastos cuyo concepto contiene la palabra."""
        resultado = []
        palabra = palabra.lower()
        for gasto in self.__gastos:
            if palabra in gasto.get_concepto().lower():
                resultado.append(gasto)
        return resultado
