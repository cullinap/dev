// ex20.js

const readline = require('readline-sync');

const say = (prompt) => {
	console.log(prompt);
}

//say('Hi');

const die = (message) => {
	say(message);
	process.exit(1);
}

//die('Noooo');

const ask = (hp, prompt) => {
	console.log(`[[You have ${hp} hit points.]]`);
	if (hp <= 0) {
		die("You died");
	} else {
		return readline.question(prompt + ' ');
	}
}

const door = (hp) => {
	// they have to open the door to get gold
	// what kind of puzzle will they solze? 
}


