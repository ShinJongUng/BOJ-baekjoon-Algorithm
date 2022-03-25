
const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
console.log("The 1-3-sum is " + (91 + input[0]*1 + input[1]*3 + input[2]*1))