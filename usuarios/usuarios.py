from mysqlconnection import connectToMySQL
DB_NAME = 'usuarios_crud'

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        #si da error, pongale data.get, asi salta al siguiente y no da error
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES (%(nombre)s, %(apellido)s,%(email)s);"
        # %(dato)s = sentencia preparada
        return connectToMySQL(DB_NAME).query_db(query, data)
 
    @classmethod
    def actualizar(cls, data):
      query = """
         UPDATE usuarios
         SET nombre = %(nombre)s,
            apellido = %(apellido)s,
            email = %(email)s
         WHERE id = %(id)s;
      """
      resultado = connectToMySQL(DB_NAME).query_db(query, data)
  
      return resultado

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL(DB_NAME).query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @classmethod
    def get_by_id(cls,datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        resultados = connectToMySQL(DB_NAME).query_db(query,datos)

        return cls(resultados[0])

    @classmethod
    def borrar(cls, datos):
      query = "DELETE FROM usuarios WHERE id = %(id)s"

      resultado = connectToMySQL(DB_NAME).query_db(query, datos)

      if resultado is False:
         raise RuntimeError("Failed to delete user")

      return resultado