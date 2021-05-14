/* ex17 */

select * from person where dob < date('now', '-10 years') order by dob;

select * from person where dob < date('1970-01-01') order by dob;

/* all pets purchaeed this year */

select * from person_pet
	where purchased_on > date('now', 'start of year')
	order by purchased_on;

/* all pets purchased between 1990 and 2000 */
select * from person
	where purchased_on > date('1990-01-01') and purchased_on < date('2000-01-01')
	order by purchased_on;

/* link the pets from the last query */
select pet.name, pet.breed, pet.age, person_pet.purchased_on
	from pet, person_pet
	where
	purchased_on > date('1990-01-01') and
	purchased_on < data('2000-01-01') and
	person_pet.pet_id = pet.id
	order by purchased_on, pet.age;

