from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def main():
    datos_conexion = r'postgresql://postgres:mcspI%1705@127.0.0.1/cursoWebCS50'
    print(datos_conexion)
    engine = create_engine(datos_conexion)
    print(engine)
    #sesion = scoped_session(sessionmaker(bind=engine))
    #resultado = sesion.execute("SELECT * FROM usuarios")
    try:
        conexion = engine.connect()
    except Exception as e:
        print(e)
        return False
    resultado = conexion.execute("select * from usuarios")
    print(resultado)
    for linea in resultado:
        print(f'{ linea.id }, {linea.usuario }, { linea.password }')

if __name__ == '__main__':
    main()