/* add a dead column to to person */
alter table person add column dead INTEGER;

/* add phone_number column to person */
alter table person add column phone_number INTEGER;

/* add salary column to person */
alter table person add column salary FLOAT;

/* add dob to person and pet */
alter table person add column dob DATETIME;
alter table pet add column dob DATETIME;

/* add purchased_on column to person_pet */
alter table person_pet add column purchased_on DATETIME;

/* add a parent column to pet that is id for pet's parent */
alter table pet add column parent INTEGER;

/* udpate the columns with new info */

select * from person;

update person
set dead = 0,
    phone_number = 777555666,
    salary = 100000,
    dob = datetime('now')
where first_name = 'Zed';

/* confirm udpate worked */
select * from person;

select * from pet;

update pet
set dob = datetime('now'),
    parent = 0 
where id in (
    select pet.id
    from pet, person_pet, person
    where
    person.id = person_pet.person_id and,
    pet.id = person_pet.pet_id and
    person.first_name = 'Zed'
);

select * from pet;

/* update purchased_on */
update person_pet
set purchased_on = datetime('now'); 
where person_id = 0;

select * from person_pet;

/* add more people into person */
insert into person (id, first_name, last_name, age, dead, phone_number,
		    salary, dob)
	values (1, 'Frank', 'Smith', 22, 0, 111, 99,
		datetime('1980-05-06 11:11:00')),
	values (2, 'Patty', 'Hearst', 20, 0, 222, 98,
		datetime('1989-05-05'))
	values (3, 'Mikal', 'g', 44, 0, 333, 100,
		datetime('1950-04-04'))
	values (4, 'mmm' 'hmmm', 55, 0, 44, 101,
		datetime('1940-03-03'));

select * from person;

insert into pet (id, name, breed, age, dead, dob, parent)
	values (2, 'Oscar', 'Dog', 2, 1, datetime('1984-05-05'), 1),
	values (3, 'Rex', 'T-Rex', 3, 0, datetime('1980-05-05'), 2),
	values (4, 'Manny', 'Cat', 2, 0, datetime('1999-02-02'), 1),
	values (5, 'Belinda', 'Anteater', 10, 1, datetime('2001-05-20'), 4)
	values (6, 'Charlie', 'Dog', 5, 0, datetime('2001-9-11'), 0);

select * from pet;





