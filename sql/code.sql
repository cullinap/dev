CREATE TABLE person (
	id INTEGER PRIMARY KEY, /* id col to identify each row */
	first_name TEXT,
	last_name TEXT,
	age INTEGER
);

CREATE TABLE pet (
	id INTEGER PRIMARY KEY,
	name TEXT,
	breed TEXT,
	age INTEGER,
	dead INTEGER
);

CREATE TABLE person_pet (
	person_id INTEGER,
	pet_id INTEGER
);

/* linking person and pet in person by adding another row to person */

insert into person (id, first_name, last_name, age)
	values (0, 'Zed', 'Shaw', 37);

insert into pet (id, name, breed, age, dead)
	values (0, 'Fluffy', 'Unicorn', 1000, 0);

insert into pet values (1, 'Gigantor', 'Robot', 1, 1);

insert into person_pet (person_id, pet_id) values (0, 1);

insert into person_pet values (0, 0);
/*make sure there is dead pets */

select name, age from pet where dead = 1;

delete from pet where dead = 1;

/* make sure robot is gone */
select * from pet;

/* bring back the robot */
insert into pet values (1, 'Gigantor', 'Robot', 1, 0);

/* check the robot again */ 
select * from pet;
select * from person;





