// ex17.js
let pigments = ["perinone", "cadium", "titanium", "ultramarine", "napthol"];

let i = 0;

while (i < pigments.length) {
	console.log(`while ${i}=${pigments[i]}`);
	i++;
}

for (let i = 0; i < pigments.length; i++) {
	console.log(`for ${i}=${pigments[i]}`);
}

for (paint of pigments) {
	console.log(`for-in ${paint}`);
}
