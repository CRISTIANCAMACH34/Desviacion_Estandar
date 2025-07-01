class Menu:
    @staticmethod
    def mostrar_menu():
        print("\n=== Menú Principal ===")
        print("1. Introducir números manualmente")
        print("2. Usar datos predefinidos")
        print("3. Ver historial de datos")
        print("4. Ver último análisis realizado")
        print("5. Reiniciar (eliminar) todos los datos")
        print("6. Salir")

    @staticmethod
    def pedir_opcion():
        return input("Seleccione una opción (1-6): ")

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
        import random
        speed = [random.randint(80, 100) for _ in range(7)]
        print(f"Datos de velocidad predefinidos (aleatorios): {speed}")
        return speed

    @staticmethod
    def mostrar_ultimo_analisis(ejecucion):
        print("\n--- Último análisis realizado ---")
        print(f"ID: {ejecucion.id}")
        print(f"Fecha: {ejecucion.fecha_ejecucion}")
        print(f"Valores: {ejecucion.data_set}")
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
    def mostrar_confirmacion_reinicio():
        return input("¿Está seguro que desea eliminar todos los datos? (s/n): ").lower() == 's'

    @staticmethod
    def mostrar_tabla_historial(ejecuciones):
        from tabulate import tabulate
        import numpy as np
        filas = []
        for i, ejecucion in enumerate(ejecuciones, 1):
            valores = [float(x) for x in ejecucion.data_set.split(',') if x.strip() != '']
            media = np.mean(valores) if valores else 0
            varianza = np.var(valores) if valores else 0
            desv_std = np.std(valores) if valores else 0
            cantidad = len(valores)
            tipo = 'predefinido' if all(80 <= v <= 100 for v in valores) and cantidad == 7 else 'manual'
            filas.append([
                i,
                tipo,
                str([round(x, 1) for x in valores]),
                f"{media:.2f}",
                f"{varianza:.2f}",
                f"{desv_std:.2f}",
                cantidad,
                str(ejecucion.fecha_ejecucion).split('.')[0]
            ])
        headers = ['#', 'Análisis', 'Dataset', 'Media', 'Var.', 'Dev.Std.', 'Cant.', 'Fecha']
        print(tabulate(filas, headers, tablefmt="grid"))

    @staticmethod
    def mostrar_tabla_ultimo(ejecucion):
        Menu.mostrar_tabla_historial([ejecucion])
