/* inserting new pesron into db so we can 
 * practice deleting them
 */

insert into person (id, first_name, last_name, age)
	values (1, 'pat', 'c', 22);

insert into pet (id, name, breed, age, dead)
	values (3, 'cal', 'fish', 2, 1);

/* connect pat and his fish */
insert into person_pet (person_id, pet_id)
	values (1,3);

/* print out person table to check */
select person.id, person.first_name from person where first_name = 'pat';

/* print out pet table */
select pet.id, pet.name from pet where id = '3';

/* now delete them */
delete from person where id in (
	select person.id
	from pet, person, person_pet
	where 
	person.id = person_pet.person_id and 
	pet.id  = person_pet.pet_id and
	person.first_name = 'pat'
);

/* check */
select * from person; 
select * from person_pet;








