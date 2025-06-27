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
    matplotlib.use('TkAgg')
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
    try:
        valores = [float(x.strip()) for x in entrada.split(',')]
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
    if not valores:
        print("No hay datos para graficar.")
        return
    plt.figure(figsize=(8, 4))
    plt.plot(valores, marker='o', linestyle='-', color='b')
    plt.title('Gráfica del Data Set')
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.show()
