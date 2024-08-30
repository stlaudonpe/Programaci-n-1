# main.py
from libreria import Libreria
from libro import Libro
from lector import Lector

# Crear una libreria con direccion y secciones
mi_libreria = Libreria(direccion="Calle Prueebas", secciones=["Ficcion", "No Ficcion", "Infantil"])

# Inicializar catalogo con 10 libros preestablecidos
mi_libreria.inicializar_catalogo()

# Registrar un lector
mi_libreria.registrar_lector("Juan Perez", "12345")

# Buscar el lector
lector = mi_libreria.buscar_lector("12345")

# Prestar un libro al lector
if lector:
    libro_a_prestar = mi_libreria.buscar_libro("El principito")
    if libro_a_prestar:
        lector.prestar_libro(libro_a_prestar)

# Listar libros prestados por el lector
lector.listar_libros_prestados()

# Devolver el libro
if libro_a_prestar:
    lector.devolver_libro(libro_a_prestar)

# Listar nuevamente los libros prestados para asegurarse de que fue devuelto
lector.listar_libros_prestados()
