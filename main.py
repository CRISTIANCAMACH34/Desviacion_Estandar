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
            valores = leer_valores_desde_consola()
            resultado = desviacion_estandar_tradicional(valores)
            Menu.mostrar_resultado(resultado)
            guardar_ejecucion(session, valores)
        elif opcion == '2':
            valores = leer_valores_desde_consola()
            resultado = desviacion_estandar_numpy(valores)
            Menu.mostrar_resultado(resultado)
            guardar_ejecucion(session, valores)
        elif opcion == '3':
            id_ejecucion = Menu.pedir_id_ejecucion()
            ejecucion = session.query(Ejecucion).filter_by(id=int(id_ejecucion)).first()
            if ejecucion:
                valores = [float(x) for x in ejecucion.data_set.split(',')]
                graficar_dataset(valores)
            else:
                Menu.mostrar_mensaje("No se encontró la ejecución con ese ID.")
        elif opcion == '4':
            Menu.mostrar_mensaje("¡Hasta luego!")
            break
        else:
            Menu.mostrar_mensaje("Opción no válida. Intente de nuevo.")
    session.close()

if __name__ == "__main__":
    main() 