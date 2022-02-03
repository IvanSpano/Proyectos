-- mostrar codigo,marca, descripción, nombre y el precio de todos los articulos
select
    codigo,
    marca,
    descripcion as linea,
    nombre as producto,
    precio as precioUnitario,
    precio*0.21 as IVA,
    precio+precio*0.21 as PrecioFinal
from articulos
order by marca desc, precioUnitario;

-- mostrar codigo, nombre y stock de los productos marca LG
-- filtrar por campos: Clausula : Where
select
	codigo,
    nombre,
    stock,
    marca
from articulos
where marca='LG';

-- traer todos los articulos con precio mayor a 1000, ordenado por descripción
select *, 'China' as Origen
from articulos
where precio >= 1000
order by descripcion;

-- traer 10 articulos mas caros
select *
from articulos
order by precio desc limit 10;


-- mostrar registros a partir de uno en particular

select *
from articulos
limit 4 offset 3;

-- funcion concat: concatenar

-- marca - nombre

select * from articulos;

select concat(marca,'-', nombre) as ARTICULO
from articulos;

-- email sea: primer letra del nombre, ., el apellido, @eduacionit.com

select * from alumnos;

select
	concat(left(nombre,1),'.', apellido,'@eduacionit.com') as Email
from alumnos;

-- filtrar registros, clausula where

-- mostrar los televisores

select * from articulos
where descripcion='televisores';


-- mostrar articulos de marca noblex y lg

select * from articulos
where marca='noblex' or marca='lg';

-- or multiples, lo simplifico con la clausula "in"

select * 
from articulos
where marca in ('noblex','lg');

-- mostrar todos los articulos excepto los de marca lg

select *
from articulos
where marca not in('lg');

-- mostrar los articulos de marca lg con stock mayor a 10

select * from articulos
where marca in('lg') and stock>10;

-- mostrar los articulos con precios mayores a 1k y menores a 2k

select * from articulos
where precio>1000 and precio<2000;

-- simplificar el and con la clausula between (incluye los extremos)

select * from articulos
where precio between 1000 and 2000;

-- mostrar telefonos sin stock

select * from articulos
where descripcion='telefonos' and stock = 0;

-- suponiendo que el punto de reposición sea 20

select * from articulos
where stock<20;

-- codigo - nombre - stock - reponer - cantidad a reponer

select
	codigo,
    nombre,
    stock,
    if (stock<20,'SI','NO') as reponer,
    if (stock<20,20-stock,0) as CantidadesAPedir
from articulos;

-- mostrar los articulos LCD

select * from articulos
where substring(nombre,4,3)="lcd";

-- busqueda por aprox/por un patron
-- mostrar todos los articulos cuyo nombre empiece con "t"

select * from articulo
where nombre like 't%';

-- traer todos los televisores de 26 pulgadas

select * from articulos
where nombre like '%26"%';

-- limitar la cantidad de registros

select * from articulos limit 38,5;

-- datos al azar

select * from articulos
order by rand() limit 6;

-- funciones de agregado o agrupamiento
-- count: retorna la cantidad de registros no nulos en un campo
-- ¿cuantos articulos tengo?

select count(precio) as Cantidad
from articulos;

-- sum: retorna la suma del contenido de un campo numero
-- ¿cuantas unidades de televisores hitachi tengo?

select count(codigo) as CantidadModelos, sum(stock) as Existencia 
from articulos
where descripcion='televisores' and marca='hitachi';

-- stock de telefonos

select sum(stock) from articulos where descripcion='telefonos';

-- max: retorna el elemento mayor de un campo numerico
-- precio mayor de los lavarropas

select max(precio) from articulos where descripcion='lavarropas';

-- min: retorna el elemento menor de un campo numerico
-- precio menor de la marca LG

select min(precio) from articulos where marca='Lg';

-- avg: retorna el promedio de un campo numero
-- promedio de precio de todos los articulos

select avg(precio) from articulos;	

-- mostrar cantidad, stock, precio max, precio min, promedio de los televisores

select 
	count(*) as Modelos,
    sum(stock) as Stock,
    max(precio) as PrecioMax,
    min(precio) as PrecioMin,
    round(avg(precio),2) as PrecioPromedio
from articulos
where descripcion='televisores';

-- mostrar cantidad, stock, precio max, precio min, promedio

select 
	descripcion as Linea,
	count(*) as Modelos,
    sum(stock) as Stock,
    max(precio) as PrecioMax,
    min(precio) as PrecioMin,
    round(avg(precio),2) as PrecioPromedio
from articulos
where marca='lg'
group by descripcion
order by stock desc;

-- cantidad de modelos por marca
-- solo las marcas que superan las 4 unidades
select
	marca,
	count(*) as Modelos
from articulos
group by marca
having count(*)>4  -- sirve como el where para las funciones. El where sirve para los campos
order by modelos desc,marca;