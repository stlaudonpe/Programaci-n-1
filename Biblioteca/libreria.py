from libro import Libro

class Libreria:
    def __init__(self, direccion, secciones):
        self.direccion = direccion
        self.secciones = secciones
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        print(f"Libro '{libro.titulo}' agregado al catalogo.")

    def eliminar_libro(self, titulo):
        libro_a_eliminar = next((libro for libro in self.catalogo if libro.titulo == titulo), None)
        if libro_a_eliminar:
            self.catalogo.remove(libro_a_eliminar)
            print(f"Libro '{titulo}' eliminado del catalogo.")
        else:
            print(f"Libro '{titulo}' no encontrado en el catalogo.")

    def mostrar_catalogo(self):
        if not self.catalogo:
            print("El catalogo esta vacio.")
        else:
            for libro in self.catalogo:
                print(libro)

    def buscar_libro(self, titulo):
        libro = next((libro for libro in self.catalogo if libro.titulo == titulo), None)
        if libro:
            print(libro)
        else:
            print(f"Libro '{titulo}' no encontrado en el catalogo.")

    def listar_prestados(self):
        libros_prestados = [libro for libro in self.catalogo if libro.prestado]
        if not libros_prestados:
            print("No hay libros prestados.")
        else:
            for libro in libros_prestados:
                print(libro)

    def inicializar_catalogo(self):
        libros_preestablecidos = [
            Libro("Don Quijote", "Miguel de Cervantes"),
            Libro("Cien anos de soledad", "Gabriel Garcia Marquez"),
            Libro("Matar a un ruisenor", "Harper Lee"),
            Libro("1984", "George Orwell"),
            Libro("El gran Gatsby", "F. Scott Fitzgerald"),
            Libro("El principito", "Antoine de Saint-Exupery"),
            Libro("Orgullo y prejuicio", "Jane Austen"),
            Libro("Crimen y castigo", "Fiodor Dostoyevski"),
            Libro("En busca del tiempo perdido", "Marcel Proust"),
            Libro("La Odisea", "Homero")
        ]
        self.catalogo.extend(libros_preestablecidos)
        print("Catalago Actual")
