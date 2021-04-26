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
/* someone who owns alot of cats 

