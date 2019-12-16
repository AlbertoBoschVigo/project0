from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class conectorDB():
    def __init__(self, usuario = 'postgres', password = '12345678', servidor = 'localhost', database = 'cursoWebCS50'):
        self.__datos_conexion = f'postgresql://{ usuario }:{ password }@{ servidor }/{ database }'
        self.__engine = create_engine(self.__datos_conexion)
        self.__sesion = scoped_session(sessionmaker(bind=self.__engine))

    def consulta(self, query):
        resultado = self.__sesion.execute(query).fetchall()
        for linea in resultado:
            print(linea)
        return resultado
        """
        try:
            conexion = engine.connect()
        except Exception as e:
            print(e)
            return False
        
        resultado = conexion.execute("select * from usuarios")
        
        #print(resultado)
        for linea in resultado:
            print(f'{ linea.id }, {linea.usuario }, { linea.password }')
        """
if __name__ == '__main__':
   conexion = conectorDB()
   #print(conexion.consulta("SELECT * FROM usuarios WHERE usuario = 'juan'"))
   print(conexion.consulta("SELECT * FROM usuarios"))