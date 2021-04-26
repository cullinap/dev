/* normal join with equality */
select pet.id, pet.name, pet.age, pet.dead 
	from pet, person_pet, person 
	where 
	pet.id = person_pet.pet_id and 
	person_pet.person_id = person.id 
	and person.first_name = 'Zed';

select pet.id, pet.name, pet.age, pet.dead 
	from pet 
	where pet.id in 
	(
		select pet_id from person_pet, person 
		where person_pet.person_id = person_id and 
		person.first_name = 'Zed'
	);