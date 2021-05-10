/* add columns to the person table */
alter table person add column age INTEGER;
alter table person add column dob DATETIME;
alter table pet add column dob DATETIME;
alter table pet add column parent INTEGER;
alter table person_pet add column purchased_on DATETIME;

