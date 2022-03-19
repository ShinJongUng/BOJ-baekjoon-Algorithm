const fs = require('fs');
let input = fs.readFileSync("ans.txt").toString().trim();

console.log((Math.pow(input, 2) * Math.PI).toFixed(6));
console.log((Math.pow(input, 2) * 2).toFixed(6));