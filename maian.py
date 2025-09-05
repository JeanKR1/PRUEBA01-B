from libro import Libro
from revista import Revista
from periodico import Periodico
from biblioteca import Biblioteca

def menu():
    print("\n===== SISTEMA BIBLIOTECA DIGITAL =====")
    print("1. Agregar material")
    print("2. Ver materiales")
    print("3. Eliminar material")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        opcion = menu()

        # 1. Agregar material
        if opcion == "1":
            print("\n--- Agregar Material ---")
            print("a) Libro")
            print("b) Revista")
            print("c) Periódico")
            tipo = input("Seleccione tipo de material: ")

            titulo = input("Título: ")
            autor = input("Autor: ")
            precio = float(input("Precio: "))

            if tipo.lower() == "a":
                paginas = int(input("Cantidad de páginas: "))
                material = Libro(titulo, autor, precio, paginas)

            elif tipo.lower() == "b":
                edicion = int(input("Número de edición: "))
                material = Revista(titulo, autor, precio, edicion)

            elif tipo.lower() == "c":
                fecha = input("Fecha de publicación (dd/mm/aaaa): ")
                material = Periodico(titulo, autor, precio, fecha)

            else:
                print("Tipo no válido.")
                continue

            biblioteca.agregar_material(material)
            print("✅ Material agregado con éxito.")

        # 2. Ver materiales (listado)
        elif opcion == "2":
            if not biblioteca.materiales:
                print("\nNo hay materiales registrados.")
            else:
                print("\n--- Lista de materiales ---")
                for i, m in enumerate(biblioteca.materiales, start=1):
                    print(f"{i}. {m.descripcion()} | Precio: ${m.get_precio()}")

        # 3. Eliminar material
        elif opcion == "3":
            if not biblioteca.materiales:
                print("\nNo hay materiales para eliminar.")
            else:
                print("\n--- Eliminar Material ---")
                for i, m in enumerate(biblioteca.materiales, start=1):
                    print(f"{i}. {m.descripcion()} | Precio: ${m.get_precio()}")

                try:
                    idx = int(input("Ingrese el número del material a eliminar: "))
                    if 1 <= idx <= len(biblioteca.materiales):
                        eliminado = biblioteca.materiales.pop(idx - 1)
                        print(f"🗑️ Se eliminó: {eliminado.descripcion()}")
                    else:
                        print("Número inválido.")
                except ValueError:
                    print("Entrada inválida.")

        # 4. Salir
        elif opcion == "4":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, intente nuevamente.")
