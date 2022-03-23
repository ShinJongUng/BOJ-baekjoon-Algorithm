let input = require("fs").readFileSync("input.txt").toString().split('');
console.log(input.sort((a,b)=> b-a).join(''))