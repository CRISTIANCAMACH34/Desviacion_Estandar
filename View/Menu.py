class Menu:
    @staticmethod
    def mostrar_menu():
        print("\n--- Cálculo de Desviación Estándar ---")
        print("1. Introducir números manualmente")
        print("2. Utilizar datos de velocidad predefinidos")
        print("3. Ver datasets guardados")
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

    @staticmethod
    def mostrar_dataset_info(ejecucion, numero_total):
        print(f"\n--- Dataset {ejecucion.id} de {numero_total} ---")
        print(f"Fecha: {ejecucion.fecha_ejecucion}")
        print(f"Valores: {ejecucion.data_set}")
        
        # Calcular la media y desviación estándar al momento de mostrar
        try:
            valores = [float(x) for x in ejecucion.data_set.split(',') if x.strip() != '']
            if valores:
                import numpy as np
                media = np.mean(valores)
                desv_std = np.std(valores)
                print(f"Media: {media:.4f}")
                print(f"Desviación estándar: {desv_std:.4f}")
            else:
                print("Media: No se pueden calcular valores")
                print("Desviación estándar: No se pueden calcular valores")
        except (ValueError, ImportError):
            print("Media: Error al calcular")
            print("Desviación estándar: Error al calcular")

    @staticmethod
    def mostrar_opciones_navegacion():
        print("\nOpciones:")
        print("'s' - Siguiente dataset")
        print("'a' - Anterior dataset")
        print("'g' - Graficar este dataset")
        print("'v' - Volver al menú principal")

    @staticmethod
    def pedir_comando_navegacion():
        return input("Ingrese comando: ").lower()

    @staticmethod
    def mostrar_mensaje_navegacion(mensaje):
        print(f"\n{mensaje}")

    @staticmethod
    def mostrar_datos_predefinidos():
        speed = [86, 87, 88, 86, 87, 85, 86]
        print(f"Datos de velocidad predefinidos: {speed}")
        return speed
