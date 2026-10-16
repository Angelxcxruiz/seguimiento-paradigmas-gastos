# Paradigma Orientado a Objetos (POO)

Implementación del Sistema de Control de Gastos Personales bajo el paradigma
orientado a objetos en Python.

## Enfoque

El paradigma orientado a objetos modela el problema mediante clases que
representan entidades del dominio. Cada objeto encapsula sus datos y ofrece
métodos para operar sobre ellos, lo que favorece la reutilización, el
mantenimiento y la organización del código.

## Estructura de clases

### Clase `Gasto`

Representa un gasto individual. Sus atributos son **privados** y solo se
accede a ellos mediante métodos accesores y mutadores.

| Elemento | Detalle |
|---|---|
| Atributos privados | `__concepto`, `__monto`, `__categoria` |
| Métodos accesores | `get_concepto()`, `get_monto()`, `get_categoria()` |
| Métodos mutadores | `set_concepto()`, `set_monto()`, `set_categoria()` con validación |
| Método especial | `__str__()` para representación legible |

### Clase `GestorGastos`

Administra la colección de objetos `Gasto`. Aplica una **relación de
composición**: el gestor *tiene* una lista de gastos.

| Método | Responsabilidad |
|---|---|
| `agregar_gasto(gasto)` | Incorpora un objeto `Gasto` a la colección |
| `get_gastos()` | Devuelve la colección completa |
| `cantidad()` | Informa cuántos gastos hay registrados |
| `calcular_total()` | Suma el monto de todos los gastos |
| `obtener_mayor()` | Devuelve el gasto con el monto más alto |
| `filtrar_por_monto(umbral)` | Devuelve los gastos mayores al umbral |
| `buscar_por_concepto(palabra)` | Devuelve coincidencias por subcadena |

## Elementos del paradigma aplicados

- **Clases:** `Gasto` y `GestorGastos`.
- **Instanciación de objetos:** en `main.py` se crean instancias de `Gasto` y
  un objeto `GestorGastos`.
- **Encapsulamiento:** atributos con doble guion bajo más métodos accesores y
  mutadores que validan los datos.
- **Métodos de instancia:** toda la lógica opera sobre objetos concretos.
- **Composición entre clases:** `GestorGastos` contiene objetos `Gasto`.

## Archivos

| Archivo | Contenido |
|---|---|
| `gasto.py` | Definición de la clase `Gasto` |
| `gestor_gastos.py` | Definición de la clase `GestorGastos` |
| `main.py` | Menú interactivo que instancia y usa los objetos |

## Ejecución

Los tres archivos deben permanecer en la misma carpeta, ya que se importan
entre sí.

```bash
python main.py
```

## Ventajas y limitaciones del paradigma

**Ventajas**
- Encapsulamiento: los datos se protegen y se validan a través de métodos.
- Reutilización y escalabilidad: las clases pueden extenderse sin reescribir la lógica.
- Organización clara del dominio del problema.
- Facilita el mantenimiento y el trabajo en equipo sobre el mismo código.

**Limitaciones**
- Mayor cantidad de estructura y código inicial para problemas pequeños.
- Curva de aprendizaje más alta frente al paradigma estructurado.
