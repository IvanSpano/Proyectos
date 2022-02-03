-- instrucciones de transaccion
-- instert into : agregar registros
-- update : modificar campos/columnas de aglun registro
-- delete : borrar  registros/filas

-- instert into: agregar registros
-- 1. Mediante valores con nombres de campo
-- 2. Mediante valores sin nombres de campo
-- 3. Mediante el select de otra tabla
-- 4. Creando la tabla de llenando con registros

-- 1. Sintaxis: insert into nombreTabla(nombreCampo1, nombrecampo2,...)
--             values(valorCampo1,valorCampo2,...)

insert into articulos(codigo,descripcion,nombre,precio,stock,marca)
values(66,'televisores','Led 32" BRAVIA',12800.56,20,'SONY');

select * from articulos;

-- 2. Sintaxis insert into nombreTabla(Valor1, Valo2,...)
insert into articulos
values(68,'televisores','FULL HD Bravia', 1600,10,'SONY');

select * from articulos;

-- 3. crear una tabla: nuevosProductos
create table nuevosProductos
(
	codigo int primary key,
    descripcion varchar(50) not null,
    nombre varchar(45) not null,
    precio float,
    stock int,
    marca varchar(45)

);

-- agregar 3 registros
INSERT INTO nuevosProductos VALUES
(100,'Televisores','TV LCD 14" MODELO ULTRA',12699,20,'PHILIPS'),
(101,'Televisores','TV LCD 18" MODELO ULTRA',15699,20,'PHILIPS'),
(102,'Televisores','TV LCD 32" MODELO ULTRA',18699,20,'PHILIPS');


-- 3. sintaxis: insert into tabla select de la otra tabla
insert into articulos
select * from nuevosProductos;

select * from articulos;

-- ir agregando al historial 
insert into historialProductos select *,current_date() from articulos;

select * from historialProductos;

-- 4. insertar registros sobre una nueva tabla: electroFest2021
-- marcas, lg(25%), noblex(22%), sanyo(19%), sony(19%)
create table electroFest2021
as
select codigo,descripcion,precio,marca
from articulos
where marca in('lg','noblex','sanyo','sony');

-- update: modificación de datos - contenido de los campos
-- sintaxis:
/* 
	update tabla
    set campo=nuevoValor
    where condiciones
*/
-- aplicar el descuento del 25% al precio de los productos lg de la tabla electrofest2021
update electrofest2021
set precio=precio*0.75
where marca='lg';

update electrofest2021
set precio=precio*0.78
where marca='noblex';

update electrofest2021
set precio=precio*0.81
where marca='sanyo' or marca='sony';

-- mostrar los porcentajes de aumento de cada articulo

-- formas de borrar datos:
-- 1. drop: Elimina el objeto
-- 2. truncate: Elimina todos los registros (reinicia el indice de auto incremental)
-- 3. delete: Elimina registros que cumplen una condición

-- drop: Elimino la tabla

drop table alumnos;


-- truncate: vaciar la tabla localidades
truncate table localidades;
select * from localidades;
insert into localidades(nombre) values('Daireaux');

delete from localidades where nombre like'd%';
-- borar las radios de marca sony
delete from electrofest2021
where descripcion='radio' and marca='sony';

select * from electrofest2021;	

set SQL_SAFE_UPDATES = 0; -- habilitar actualizaciones o eliminaciones masivas

