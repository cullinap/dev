/* this should fail */
insert into person (id, first_name, last_name, age)
	values (0, 'Frank', 'Smith', 100);

insert or replace into person (id, first_name, last_name, age)
	values (0, 'Frank', 'Smith', 100);

select * from person;

/* shorthand for just replace */
replace into person (id, first_name, last_name, age)
	values (0, 'Zed', 'Shaw', 44);

/* now you can see I'm back */
select * from person;

/* now replace unicorn with pet parrot */
insert or replace into pet (id, name, breed, age, dead)
	values (0, 'pete', 'parrot', 5, 0);

/* shoe the replacement */
select * from pet;

/* bring back to normal */
replace into pet (id, name, breed, age, dead)
	values (0, 'Fluffy', 'Unicorn', 1000, 0);

select * from pet;	




