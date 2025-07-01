# NOTA: Asegúrese de tener instalados numpy y sqlalchemy en su entorno:
# pip install numpy sqlalchemy
try:
    import numpy as np
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from Model.Model_Metodo_Tradicional import Ejecucion, Base
    import datetime
    import matplotlib.pyplot as plt
    import matplotlib
    try:
        matplotlib.use('TkAgg')
    except Exception:
        print("Advertencia: No se pudo establecer el backend interactivo para matplotlib. Puede que la gráfica no se muestre correctamente.")
except ImportError as e:
    print(f"Error de importación: {e}. Instale las dependencias necesarias.")

# Método tradicional para calcular la desviación estándar
def desviacion_estandar_tradicional(valores):
    n = len(valores)
    if n == 0:
        return None
    media = sum(valores) / n
    suma_cuadrados = sum((x - media) ** 2 for x in valores)
    return (suma_cuadrados / n) ** 0.5

# Método usando numpy para calcular la desviación estándar
def desviacion_estandar_numpy(valores):
    if len(valores) == 0:
        return None
    return np.std(valores)

# Función para leer valores desde la consola
# (puedes llamarla desde un main o desde otro script)
def leer_valores_desde_consola():
    entrada = input("Ingrese los valores separados por comas: ")
    if not entrada.strip():
        print("Error: No se ingresaron valores.")
        return []
    try:
        valores = [float(x.strip()) for x in entrada.split(',') if x.strip() != '']
        if not valores:
            print("Error: No se ingresaron valores válidos.")
        return valores
    except ValueError:
        print("Error: asegúrese de ingresar solo números separados por comas.")
        return []

# Función para guardar la ejecución en la base de datos
def guardar_ejecucion(session, data_set):
    ejecucion = Ejecucion(
        fecha_ejecucion=datetime.datetime.utcnow(),
        data_set=','.join(str(x) for x in data_set)
    )
    session.add(ejecucion)
    session.commit()
    return ejecucion

def graficar_dataset(valores):
    if not valores or not all(isinstance(x, (int, float)) for x in valores):
        print("No hay datos numéricos válidos para graficar.")
        return
    try:
        # Calcular estadísticas para mostrar en el gráfico
        import numpy as np
        media = np.mean(valores)
        desv_std = np.std(valores)
        
        plt.figure(figsize=(10, 6))
        
        # Gráfico principal de los valores
        plt.subplot(2, 1, 1)
        plt.plot(valores, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
        plt.axhline(y=media, color='red', linestyle='--', label=f'Media: {media:.2f}')
        plt.title('Análisis de Desviación Estándar', fontsize=14, fontweight='bold')
        plt.xlabel('Índice de los datos')
        plt.ylabel('Valores')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Gráfico de barras mostrando la desviación
        plt.subplot(2, 1, 2)
        indices = range(len(valores))
        plt.bar(indices, valores, color='skyblue', alpha=0.7)
        plt.axhline(y=media, color='red', linestyle='--', label=f'Media: {media:.2f}')
        plt.title(f'Distribución de Datos - Desviación Estándar: {desv_std:.4f}')
        plt.xlabel('Índice de los datos')
        plt.ylabel('Valores')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # Mostrar resumen de estadísticas
        print(f"\n--- Resumen Estadístico ---")
        print(f"Valores: {valores}")
        print(f"Media: {media:.4f}")
        print(f"Desviación Estándar: {desv_std:.4f}")
        print(f"Número de datos: {len(valores)}")
        
    except Exception as e:
        print(f"No se pudo mostrar la gráfica: {e}")
