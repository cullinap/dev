// exercise 5
const invincible = 94;
let changeme = 82;

console.log(`invincible=${invincible} but changeme=${changeme}`);

// this will work fine
changeme = 100;

// uncomment this to see how you can't do this 
// invincible = 10000;

console.log(`After change: invincible=${invincible} but changeme=${changeme}`);