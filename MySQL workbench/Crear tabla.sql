-- crear una tabla : Nombre: alumnos
-- campos: dni - apellido - nombre
-- PK: dni
-- activo la bae de datos: agosto23
use agosto23;
create table alumnos
(
     -- campos
     dni int primary key,
     apellido varchar(40) not null,
     nombre varchar(40)
);