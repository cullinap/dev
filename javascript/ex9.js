// ex9.js 
const fs = require("fs");

let contents = fs.readFileSync("test.txt");

console.log("Contents:");
console.log(contents.toString());

// compact
console.log("-----------------")
console.log(fs.readFileSync("test.txt").toString())


// using a callback 
console.log("-----------------");
fs.readFile("test.txt", (err, data) => {
	let variable = 2;
	console.log(data.toString());
	//console.log(variable);
});