/* add columns to the person table */
alter table person add column dead INTEGER;
alter table person add column phone_number INTEGER;
alter table person add column salary FLOAT;
alter table person add column dob DATETIME;
alter table pet add column dob DATETIME;
alter table pet add column parent INTEGER;
alter table person_pet add column purchased_on DATETIME;

/* update person and pet with new column info */
update person
set dead = 0,
    phone_number = 10,
    salary = 9,
    dob = datetime('1980-01-01')
where first_name = 'Zed'; 

update pet
set dob = datetime('now'),
    parent = 0
where id in (
    select pet.id
    from pet, person_pet, person
    where
    person.id = person_pet.person_id and
    pet.id = person_pet.pet_id and
    person.first_name = 'Zed'
);

update person_pet set purchased_on = datetime('2010-01-01')
    where person_id = 0;

/* check that columns got added */
select * from person;
select * from pet;
select * from person_pet;

/* add more people and pets to the table */
insert into person(id, first_name, last_name, age, dead, phone_number, salary, dob)    values 
        (1, 'Frank', 'Smith', 22, 0, 111, 99, datetime('1989-05-06')),
	(2, 'Patty', 'Hearst', 20, 0, 222, 98, datetime('1988-02-02')),
        (3, 'Mikal', 'g', 44, 0, 333, 100, datetime('1950--04-04')),
	(4, 'mmm','hmmm', 55, 0, 44, 101, datetime('1940-03-03'));

insert into pet(id, name, breed, age, dead, dob, parent)
    values 
	(2, 'Oscar', 'Dog', 2, 1, datetime('1984-05-05'), 1),
	(3, 'Rex', 'T-Rex', 3, 0, datetime('1988-05-05'), 2),
	(4, 'Manny', 'Cat', 2, 0, datetime('1999-02-02'), 1),
	(5, 'Alister', 'Anteaster', 1, 0, datetime('2001-05-20'), 4),
	(6, 'Charlie', 'Dog', 5, 0, datetime('2020-09-11'), 2);

insert or replace into person_pet(person_id, pet_id, purchased_on)
    values 
	(1,2, datetime('2002-02-02')),
	(2,3, datetime('2001-01-01')),
	(2,4, datetime('1985-01-05')),
	(4,5, datetime('2000-02-02')),
	(2,6, datetime('2100-02-02')); 

select * from person;
select * from pet;
select * from person_pet;

select pet.id, pet.name, person.first_name, person_pet.purchased_on
from pet, person_pet, person
where 
    pet.id = person_pet.pet_id and
    person_pet.person_id = person.id and
    person_pet.purchased_on > datetime('2004-01-01');  
 







