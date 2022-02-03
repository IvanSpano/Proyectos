-- agregamos 3 marcas
insert into marcas(nombre) values('ASUS');
insert into marcas(nombre) values('logitech');
insert into marcas(nombre) values('genius');

/* asignar distintos origenes
 id: 1,2,3,5,7: JAPON
 id: 4,6,8,9,10: ALEMANIA
 id: 11,12,13,15,17,18: USA
 id: 14,16,19,20,21: CHINA
 */
update marcas
set origen='JAPON'
where id in(1,2,3,5,7);

update marcas
set origen='ALEMANIA'
where id in(4,6,8,9,10);

update marcas
set origen='USA'
where id in(11,12,13,15,17,18);

update marcas
set origen='CHINA'
where id in(14,16,19,20,21);

select * from marcas