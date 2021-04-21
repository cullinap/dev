CREATE TABLE person (
	id INTEGER PRIMARY KEY, /* id col to identify each row */
	first_name TEXT,
	last name TEXT,
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

CREATE TABLE cars (
	id INTEGER PRIMARY KEY,
	car_make TEXT,
	car_year INTEGER
)

CREATE TABLE person_car (
	person_id INTEGER,
	car_id INTEGER
)


/* linking person and pet in person by adding another row to person */
/* someone who owns alot of cats 

