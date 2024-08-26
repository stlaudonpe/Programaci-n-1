from libro import Libro

class Lector:
    def __init__(self, nombre, carnet):
        self.__nombre = nombre
        self.__carnet = carnet
        self.__libros_prestados = []

    def __str__(self):
        return f"Lector: {self.__nombre} (Carnet: {self.__carnet})"

    def prestar_libro(self, libro):
        if libro.is_prestado():
            print(f"El libro '{libro.get_titulo()}' ya está prestado.")
        else:
            libro.prestar_libro("fecha_devolucion")
            self.__libros_prestados.append(libro)
            print(f"Libro '{libro.get_titulo()}' prestado a {self.__nombre}.")

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            libro.devolver_libro()
            self.__libros_prestados.remove(libro)
            print(f"Libro '{libro.get_titulo()}' devuelto por {self.__nombre}.")
        else:
            print(f"El libro '{libro.get_titulo()}' no fue prestado a {self.__nombre}.")

    def listar_libros_prestados(self):
        if not self.__libros_prestados:
            print(f"{self.__nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {self.__nombre}:")
            for libro in self.__libros_prestados:
                print(f"- {libro.get_titulo()}")
