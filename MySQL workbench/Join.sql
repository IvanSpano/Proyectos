/* relaciones entre las tablas: joins
   1. inner join: Lo común entre las 2 tablas
   2. outer joins: 
		2.1 left join: Lo común + lo no común de la tabla de la izquierda
        2.2 right join: Lo común + lo no común de la tabla de la derecha
   3. cross joins: producto cartesiano (cada registro de la izq * cada registro de la derecha)
   4. full joins: left + right
   5. self joins: join sobre la misma tabla
*/

/* inner join
 mostrar campos de las 2 tablas relacionadas
 filtrar por campos de cualquiera de las dos tablas
 sintaxis:
 select campos, ....
 from tabla1 as t1
 inner join tabla2 as t2 on t1.campocomunt1=t2.campocomunt2
 */
 select
	a.codigo,
    a.nombre articulo,
    m.nombre marca,
    a.precio
 from articulos a
 inner join marcas m on a.idMarca=m.id
 where m.origen='CHINA';  -- para mostrar los articulos especificos de china
 
 -- left join
 
  select
	a.codigo,
    a.nombre articulo,
    m.nombre marca,
    a.precio
 from articulos a
 left join marcas m on a.idMarca=m.id;
 
 -- cross join
 select
	a.codigo,
    a.nombre articulo,
    m.nombre marca,
    a.precio
 from articulos as a
 cross join marcas as m;
 
 -- full join (no funciona en mysql, hay que hacer right + left join.
 
  select
	a.codigo,
    a.nombre articulo,
    m.nombre marca,
    a.precio
 from marcas as m
 full outer  join articulos as a on a.idMarca=m.id;