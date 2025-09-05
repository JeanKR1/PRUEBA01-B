class Material:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio  # atributo encapsulado

    # Getter
    def get_precio(self):
        return self.__precio

    # Setter con validación
    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que 0")

    # Método polimórfico (será sobrescrito)
    def descripcion(self):
        return f"Material: Título '{self.titulo}', Autor {self.autor}"

