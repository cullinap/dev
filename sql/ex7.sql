/* make sure there is dead pets */
select name, age from pet where dead = 1;

delete from pet where dead = 1;

/* make sure robot is gone */
select * from pet;

/* bring back the robot */
insert into pet values (1, 'Gigantor', 'Robot', 1, 0);

/* check the robot again */ 
select * from pet;