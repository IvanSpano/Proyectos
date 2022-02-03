create table marcas
(
	id int auto_increment primary key,
    nombre varchar(50) not null,
    origen varchar(50)
);

insert into marcas(nombre)
select distinct marca from articulos
order by marca;

select * from marcas;

ALTER TABLE marcas 
ADD UNIQUE INDEX `nombre_UNIQUE` (`nombre` ASC);  -- protege el campo nombre para que no permita duplicados

-- agregar un campo idMarca int despues del campo marca

alter table articulos
add column idMarca int null after marca;

-- campo comun articulos: marca, marcas: nombre
update articulos as a
join marcas as m on a.marca=m.nombre
set a.idMarca=m.id; 
select * from articulos;

-- borrar campo marca de articulos

alter table articulos
drop column marca;

-- crear la clave foranea - foreign key - FK. Sirve para relacionar y mantener la integridad de los datos
alter table articulos
add constraint fk_marcas
foreign key(idMarcas)
references marcas(id)
on update no action
on delete no action;

