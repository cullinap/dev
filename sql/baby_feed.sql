CREATE TABLE feed ( 
	id INTEGER PRIMARY KEY,
	time DATETIME,
	oz INTEGER,
	diaper INTEGER
);

/* diaper = 0: nothing, 1: wet 2: poo */

insert into feed (id, time, oz, diaper)
	values (0, datetime('2021-05-11 04:00'), 4, 2)


