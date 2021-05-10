// Exercise 12: Functions, files, and variables

// import fs module
const fs = require('fs');

// takes data and prints 
const print_lines = (err, data) => {
	console.log(data.toString());
}

// takes data and returns upper case 
const yell_at_me = (what) => {
	return what.toUpperCase();
}

const whisper = (what) => {
	console.log("Now I'm whispering");
	console.log("\n");
	return what.toLowerCase();
}

// reads file and prints text?
fs.readFile("poem.txt", print_lines);

// takes poem, upper cases it and then prints lines using an anonymous cb fn
fs.readFile("poem.txt", (err,data) => {
	let yelling = yell_at_me(data.toString());
	let whispering = whisper(yelling);
	print_lines(err, yell_at_me(whispering);
});


