class Libro:
    def __init__(self, titulo, autor, prestado=False, fecha_devolucion=None):
        self.__titulo = titulo
        self.__autor = autor
        self.__prestado = prestado
        self.__fecha_devolucion = fecha_devolucion

    def __str__(self):
        prestado_str = "Si" if self.__prestado else "No"
        return f"'{self.__titulo}' por {self.__autor} - Prestado: {prestado_str}, Fecha de devolucion: {self.__fecha_devolucion or 'N/A'}"

    def prestar_libro(self, fecha_devolucion):
        if not self.__prestado:
            self.__prestado = True
            self.__fecha_devolucion = fecha_devolucion
            print(f"El libro '{self.__titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.__titulo}' ya esta prestado.")

    def devolver_libro(self):
        if self.__prestado:
            self.__prestado = False
            self.__fecha_devolucion = None
            print(f"El libro '{self.__titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.__titulo}' no estaba prestado.")

    # Metodos getters para acceder a los atributos privados si es necesario
    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def is_prestado(self):
        return self.__prestado
