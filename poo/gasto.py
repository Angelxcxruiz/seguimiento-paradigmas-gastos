# ============================================================
# Sistema de Control de Gastos Personales
# Paradigma: ORIENTADO A OBJETOS (POO)
# Archivo: gasto.py
#
# Clase que representa un gasto individual.
# Aplica ENCAPSULAMIENTO: los atributos son privados (doble
# guion bajo) y solo se accede a ellos mediante metodos
# accesores (getters) y mutadores (setters).
# ============================================================


class Gasto:
    """Representa un gasto con concepto, monto y categoria."""

    def __init__(self, concepto, monto, categoria):
        # Atributos privados: no se acceden desde fuera de la clase
        self.__concepto = concepto
        self.__monto = monto
        self.__categoria = categoria

    # ---------------- Metodos accesores (getters) ----------------

    def get_concepto(self):
        """Devuelve el concepto del gasto."""
        return self.__concepto

    def get_monto(self):
        """Devuelve el monto del gasto."""
        return self.__monto

    def get_categoria(self):
        """Devuelve la categoria del gasto."""
        return self.__categoria

    # ---------------- Metodos mutadores (setters) ----------------

    def set_concepto(self, concepto):
        """Modifica el concepto validando que no quede vacio."""
        if concepto.strip() == "":
            raise ValueError("El concepto no puede estar vacio.")
        self.__concepto = concepto

    def set_monto(self, monto):
        """Modifica el monto validando que sea mayor que cero."""
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")
        self.__monto = monto

    def set_categoria(self, categoria):
        """Modifica la categoria del gasto."""
        if categoria.strip() == "":
            raise ValueError("La categoria no puede estar vacia.")
        self.__categoria = categoria

    # ---------------- Metodo de instancia especial ----------------

    def __str__(self):
        """Representacion legible del objeto Gasto."""
        return f"{self.__concepto} ({self.__categoria}): ${self.__monto:.2f}"
