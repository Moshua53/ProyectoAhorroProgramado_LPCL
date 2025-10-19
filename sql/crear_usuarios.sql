
-- Crea la tabla de usuarios
create table usuarios (
  cedula varchar( 20 )  NOT NULL PRIMARY KEY,
  nombre text not null,
  apellido text not null,
  correo text
); 