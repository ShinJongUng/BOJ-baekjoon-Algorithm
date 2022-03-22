const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');


console.log(stdin.join("\n"))