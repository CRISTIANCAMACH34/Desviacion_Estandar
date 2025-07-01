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
            # Mostrar historial de datos en formato tabla
            ejecuciones = session.query(Ejecucion).order_by(Ejecucion.id).all()
            if not ejecuciones:
                Menu.mostrar_mensaje("No hay datasets guardados.")
                continue
            Menu.mostrar_tabla_historial(ejecuciones)
            # Mantener la navegación interactiva si lo deseas, o solo mostrar la tabla
        elif opcion == '4':
            # Ver último análisis realizado en formato tabla
            ejecucion = session.query(Ejecucion).order_by(Ejecucion.id.desc()).first()
            if ejecucion:
                Menu.mostrar_tabla_ultimo(ejecucion)
            else:
                Menu.mostrar_mensaje("No hay análisis realizados.")
        elif opcion == '5':
            # Reiniciar (eliminar) todos los datos
            if Menu.mostrar_confirmacion_reinicio():
                session.query(Ejecucion).delete()
                session.commit()
                Menu.mostrar_mensaje("Todos los datos han sido eliminados.")
            else:
                Menu.mostrar_mensaje("Operación cancelada.")
        elif opcion == '6':
            Menu.mostrar_mensaje("¡Hasta luego!")
            break
        else:
            Menu.mostrar_mensaje("Opción no válida. Intente de nuevo.")
    session.close()

if __name__ == "__main__":
    main() 