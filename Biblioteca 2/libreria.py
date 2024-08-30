# libreria.py
from libro import Libro
from lector import Lector

class Libreria:
    def __init__(self, direccion, secciones):
        self.__direccion = direccion
        self.__secciones = secciones
        self.__catalogo = []
        self.__lectores = []

    def agregar_libro(self, libro):
        self.__catalogo.append(libro)

    def eliminar_libro(self, titulo):
        # Usamos 'if' en lugar de 'si'
        self.__catalogo = [libro for libro in self.__catalogo if libro.get_titulo() != titulo]

    def mostrar_catalogo(self):
        for libro in self.__catalogo:
            print(libro)

    def inicializar_catalogo(self):
        libros_preestablecidos = [
            Libro("Don Quijote", "Miguel de Cervantes"),
            Libro("Cien años de soledad", "Gabriel García Márquez"),
            Libro("Matar a un ruiseñor", "Harper Lee"),
            Libro("1984", "George Orwell"),
            Libro("El gran Gatsby", "F. Scott Fitzgerald"),
            Libro("El principito", "Antoine de Saint-Exupéry"),
            Libro("Orgullo y prejuicio", "Jane Austen"),
            Libro("Crimen y castigo", "Fiódor Dostoyevski"),
            Libro("En busca del tiempo perdido", "Marcel Proust"),
            Libro("La Odisea", "Homero")
        ]
        self.__catalogo.extend(libros_preestablecidos)

    def registrar_lector(self, nombre, carnet):
        lector = Lector(nombre, carnet)
        self.__lectores.append(lector)
        print(f"Lector '{nombre}' registrado con carnet '{carnet}'.")

    def buscar_lector(self, carnet):
        # Usamos 'if' en lugar de 'si'
        return next((lector for lector in self.__lectores if lector.get_carnet() == carnet), None)

    def buscar_libro(self, titulo):
        # Usamos 'if' en lugar de 'si'
        return next((libro for libro in self.__catalogo if libro.get_titulo() == titulo), None)
