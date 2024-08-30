# libro.py

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__prestado = False
        self.__fecha_devolucion = None

    def __str__(self):
        return f"{self.__titulo} por {self.__autor}"

    def prestar_libro(self, fecha_devolucion):
        self.__prestado = True
        self.__fecha_devolucion = fecha_devolucion

    def devolver_libro(self):
        self.__prestado = False
        self.__fecha_devolucion = None

    def is_prestado(self):
        return self.__prestado

    def get_titulo(self):
        return self.__titulo

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion
