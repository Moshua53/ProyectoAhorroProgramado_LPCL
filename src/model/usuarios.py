
class Usuario:

    def __init__( self, cedula, nombre, apellido, correo, direccion, telefono, codigo_departamento, codigo_municipio )  :
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def is_equal( self, comparar_con ) :

        assert( self.cedula == comparar_con.cedula )
        assert( self.nombre == comparar_con.nombre )
        assert( self.apellido== comparar_con.apellido )
        assert( self.correo== comparar_con.correo )