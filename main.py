from Controller.Controller_Metodo_Tradicional import (
    desviacion_estandar_tradicional,
    desviacion_estandar_numpy,
    leer_valores_desde_consola,
    guardar_ejecucion,
    graficar_dataset
)
from View.Menu import Menu
from Model.Model_Metodo_Tradicional import Base, Ejecucion
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

try:
    from Desviacion_Estandar import config
except ImportError:
    import config

# Crear la conexión a la base de datos
engine = create_engine(config.SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main():
    session = Session()
    while True:
        Menu.mostrar_menu()
        opcion = Menu.pedir_opcion()
        if opcion == '1':
            # Opción 1: Introducir números manualmente
            valores = leer_valores_desde_consola()
            if valores:
                resultado = desviacion_estandar_numpy(valores)
                Menu.mostrar_resultado(resultado)
                guardar_ejecucion(session, valores)
                # Visualizar resultados con Matplotlib
                graficar_dataset(valores)
        elif opcion == '2':
            # Opción 2: Utilizar datos de velocidad predefinidos
            valores = Menu.mostrar_datos_predefinidos()
            resultado = desviacion_estandar_numpy(valores)
            Menu.mostrar_resultado(resultado)
            guardar_ejecucion(session, valores)
            # Visualizar resultados con Matplotlib
            graficar_dataset(valores)
        elif opcion == '3':
            # Obtener todos los datasets ordenados por ID
            ejecuciones = session.query(Ejecucion).order_by(Ejecucion.id).all()
            
            if not ejecuciones:
                Menu.mostrar_mensaje("No hay datasets guardados.")
                continue
            
            indice_actual = 0
            total_ejecuciones = len(ejecuciones)
            
            while True:
                ejecucion_actual = ejecuciones[indice_actual]
                Menu.mostrar_dataset_info(ejecucion_actual, total_ejecuciones)
                Menu.mostrar_opciones_navegacion()
                
                comando = Menu.pedir_comando_navegacion()
                
                if comando == 's':  # Siguiente
                    if indice_actual < total_ejecuciones - 1:
                        indice_actual += 1
                    else:
                        Menu.mostrar_mensaje_navegacion("Ya estás en el último dataset.")
                
                elif comando == 'a':  # Anterior
                    if indice_actual > 0:
                        indice_actual -= 1
                    else:
                        Menu.mostrar_mensaje_navegacion("Ya estás en el primer dataset.")
                
                elif comando == 'g':  # Graficar
                    try:
                        valores = [float(x) for x in ejecucion_actual.data_set.split(',') if x.strip() != '']
                        graficar_dataset(valores)
                    except ValueError:
                        Menu.mostrar_mensaje("El data set guardado contiene valores no numéricos.")
                
                elif comando == 'v':  # Volver
                    break
                
                else:
                    Menu.mostrar_mensaje_navegacion("Comando no válido. Use 's', 'a', 'g' o 'v'.")
        elif opcion == '4':
            Menu.mostrar_mensaje("¡Hasta luego!")
            break
        else:
            Menu.mostrar_mensaje("Opción no válida. Intente de nuevo.")
    session.close()

if __name__ == "__main__":
    main() 