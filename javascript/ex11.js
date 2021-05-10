// ex11.js
//
const printPerson = (name, age) => {
	console.log(`Hi ${name}, you are ${age} years old.`);
}

printPerson('Zed', 44);
printPerson('Fran', 32);
printPerson('Steve', 22);
printPerson('Olivia', 18);

console.log('---------------- pets ------------------');

const printPet = (owner_name, owner_age, pet_name, pet_age) => {
	printPerson(owner_name, owner_age);
	console.log(`That person owns ${pet_name} who is ${pet_age} years old.`);
}

printPet('Zed',  44, 'Mr. Scruffles', 10);
printPet('Fran', 32, 'Crazy', 2);
printPet('Alex', 30, 'Lizzy Lizard', 1);
printPet('Eve', 35, 'Kong the donkey', 20);

console.log('---------------- callback style -------------------');

const fancyPet = (owner_name, owner_age, pet_name, pet_age, cb) => {
	cb(owner_name, owner_age);
	console.log(`that person owns ${pet_name} who is ${pet_age} years old`);
}

fancyPet('Zed', 44, 'Mr. Scruffles', 10, (name, age) => {
	console.log(`Ooooh fancy ${name} you are ${age} old.`);
});

fancyPet('Zed', 2, 'Mr. Scruffles', 10, (x,y) => {
	console.log(`ooooh fancy2 ${x} and ${y}`)
});

