import Teclado

# Lista que almacenará los nombres de las personas
personas = []

# Función para crear una persona
def crear_persona():
    nombre = Teclado.Teclado.read_text("Ingrese el nombre de la persona:", min_length=1, max_length=50)
    personas.append(nombre)
    print(f"Persona '{nombre}' creada exitosamente.")


# Función para leer las personas
def leer_personas():
    # Verifica si hay personas registradas
    if not personas:
        print("No hay personas registradas.")
    else:
        print("Listado de personas:")
        for indice, nombre in enumerate(personas):
            print(f"{indice}. {nombre}")


# Función para actualizar una persona
def actualizar_persona():
    # Verifica si hay personas registradas
    if not personas:
        print("No hay personas registradas para actualizar.")
        return
    leer_personas()  # Mostrar la lista para que el usuario seleccione el índice correcto
    indice = Teclado.Teclado.read_integer("Ingrese el índice de la persona a actualizar:",
                                  min_value=0, max_value=len(personas) - 1)
    nuevo_nombre = Teclado.Teclado.read_text("Ingrese el nuevo nombre:", min_length=1, max_length=50)
    personas[indice] = nuevo_nombre
    print(f"Persona en el índice {indice} actualizada a '{nuevo_nombre}'.")


# Función para eliminar una persona
def eliminar_persona():
    # Verifica si hay personas registradas
    if not personas:
        print("No hay personas registradas para eliminar.")
        return
    leer_personas()
    indice = Teclado.Teclado.read_integer("Ingrese el índice de la persona a eliminar:",
                                  min_value=0, max_value=len(personas)-1)
    # Confirmación de acción de eliminar
    if Teclado.Teclado.read_boolean("¿Está seguro de que desea eliminar la persona?"):
        eliminado = personas.pop(indice)
        print(f"Persona '{eliminado}' eliminada exitosamente.")
    else:
        print("Operación cancelada.")


# Función principal que muestra el menú y gestiona las opciones
def main():
    while True:
        print("\n--- Menú CRUD de Personas ---")
        print("1. Leer personas")
        print("2. Crear persona")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Salir")
        opcion = Teclado.Teclado.read_integer("Seleccione una opción (1-5):", min_value=1, max_value=5)

        if opcion == 1:
            leer_personas()
        elif opcion == 2:
            crear_persona()
        elif opcion == 3:
            actualizar_persona()
        elif opcion == 4:
            eliminar_persona()
        elif opcion == 5:
            # Confirmación antes de acción de salir
            if Teclado.Teclado.read_boolean("¿Está seguro de que desea salir del programa?"):
                print("Saliendo del programa...")
                break
            else:
                print("Operación cancelada. Regresando al menú.")


if __name__ == '__main__':
    main()