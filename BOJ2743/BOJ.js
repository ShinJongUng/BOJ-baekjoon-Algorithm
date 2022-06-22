const filePath = process.platform === 'linux' ? '/dev/stdin' : './ans.txt';
let input = require('fs').readFileSync(filePath).toString().trim().split("\n");
console.log(input.join('').length)