class Biblioteca:
    def __init__(self):
        self.materiales = []

    def agregar_material(self, material):
        self.materiales.append(material)

    def mostrar_catalogo(self):
        print("\n--- Catálogo de la Biblioteca ---")
        total = 0
        for m in self.materiales:
            print(f"{m.descripcion()} | Precio: ${m.get_precio()}")
            total += m.get_precio()
        print(f"\nValor total del catálogo: ${total}")
