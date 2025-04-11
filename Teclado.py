class Teclado:
    @staticmethod
    def _validate_length(input_str, min_length, max_length):
        """
        Valida que la longitud del texto del input esté entre el rango de longitudes,
        si alguno de los límites es None, se ignora esa verificación.
        """
        if min_length is not None and len(input_str) < min_length:
            return False
        if max_length is not None and len(input_str) > max_length:
            return False
        return True

    @staticmethod
    def _validate_range(value, min_value, max_value):
        """
        Valida que el valor numérico esté dentro del rango,
        si alguno de los límites es None, se ignora esa verificación.
        """
        if min_value is not None and value < min_value:
            return False
        if max_value is not None and value > max_value:
            return False
        return True

    @staticmethod
    def read_double(mensaje, min_length=None, max_length=None, min_value=None, max_value=None):
        """
        Validar un número decimal desde el input:
          - Que cumpla con la longitud indicada
          - Que el número esté dentro del rango de valores especificados
        """
        while True:
            entrada = input(mensaje + "\n")
            try:
                numero = float(entrada)
                num_str = str(numero)
                if not Teclado._validate_length(num_str, min_length, max_length):
                    print(f"El número debe tener entre {min_length} y {max_length} dígitos.")
                    continue
                if not Teclado._validate_range(numero, min_value, max_value):
                    rango = []
                    if min_value is not None:
                        rango.append(f"mayor o igual que {min_value}")
                    if max_value is not None:
                        rango.append(f"menor o igual que {max_value}")
                    print("El número debe ser " + " y ".join(rango) + ".")
                    continue
                return numero
            except ValueError:
                print("Eso no es un número válido. Intentá de nuevo:")

    @staticmethod
    def read_integer(mensaje, min_length=None, max_length=None, min_value=None, max_value=None):
        """
        Lee un número entero desde el input y valida lo siguiente:
          - Que cumpla con la longitud indicada
          - Que el número esté dentro del rango de valores especificados
        """
        while True:
            entrada = input(mensaje + "\n")
            try:
                numero = int(entrada)
                num_str = str(numero)
                if not Teclado._validate_length(num_str, min_length, max_length):
                    print(f"El número debe tener entre {min_length} y {max_length} dígitos.")
                    continue
                if not Teclado._validate_range(numero, min_value, max_value):
                    rango = []
                    if min_value is not None:
                        rango.append(f"mayor o igual que {min_value}")
                    if max_value is not None:
                        rango.append(f"menor o igual que {max_value}")
                    print("El número debe ser " + " y ".join(rango) + ".")
                    continue
                return numero
            except ValueError:
                print("Eso no es un número válido. Intentá de nuevo:")

    @staticmethod
    def read_text(mensaje, min_length=None, max_length=None):
        """
        Lee un texto desde el input y se asegura de que no esté vacío,
        validando además la longitud si se especifica.
        """
        while True:
            texto = input(mensaje + "\n").strip()
            if texto and Teclado._validate_length(texto, min_length, max_length):
                return texto
            print(f"El texto debe tener entre {min_length} y {max_length} caracteres.")

    @staticmethod
    def read_boolean(mensaje):
        """
        Método para leer un booleano usando "Sí/No" o "1/0".
        """
        while True:
            entrada = input(mensaje + " (Sí/No o 1/0):\n").strip().lower()
            if entrada in ["sí", "si", "s", "1"]:
                return True
            elif entrada in ["no", "n", "0"]:
                return False
            else:
                print("Solo podés meter 'Sí' o 'No', o si te da pereza, un '1' o '0'. Probá otra vez:")
