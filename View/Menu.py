class Menu:
    @staticmethod
    def mostrar_menu():
        print("\n--- Cálculo de Desviación Estándar ---")
        print("1. Calcular desviación estándar (método tradicional)")
        print("2. Calcular desviación estándar (usando numpy)")
        print("3. Graficar un data set guardado")
        print("4. Salir")

    @staticmethod
    def pedir_opcion():
        return input("Seleccione una opción: ")

    @staticmethod
    def mostrar_resultado(resultado):
        print(f"La desviación estándar es: {resultado}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

    @staticmethod
    def pedir_id_ejecucion():
        return input("Ingrese el ID de la ejecución a graficar: ")
