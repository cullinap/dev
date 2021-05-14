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

const spider = (hp) => {
	// they enter here, and the spider takes 10 hit points
	// if they live then they can run away
}

const gold = (hp) => {
	// end of the game they win if they get the gold 
}

const rope = (hp) => {
	
}

const well = (hp) => {
	say("You are walking through the woods and see a well");
	say("Walking up to it and looking down you see a shiny thing at the bottom");
	let next = ask(hp, "What do you do?");

	if (next == "climb") {
		say("You climb down the rope");
		rope(hp);
	} else if(next == "jump") {
		say("Yikes! Let's see if you survive!");
		hp = Math.floor(hp / 2);
		rope(hp);
	} else {
		say("You can't do that here.");
		well(hp);
	}
}

let hp = Math.floor(Math.random() * 10) + 1;



