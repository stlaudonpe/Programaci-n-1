from libreria import Libreria
from libro import Libro
from lector import Lector


mi_libreria = Libreria(direccion="Calle tepito", secciones=["Ficción", "No Ficción", "Infantil"])

mi_libreria.inicializar_catalogo()

mi_libreria.registrar_lector("Juan Pérez", "12345")

lector = mi_libreria.buscar_lector("12345")

if lector:
    libro_a_prestar = mi_libreria.buscar_libro("El principito")
    if libro_a_prestar:
        lector.prestar_libro(libro_a_prestar)

lector.listar_libros_prestados()

if libro_a_prestar:
    lector.devolver_libro(libro_a_prestar)

lector.listar_libros_prestados()