const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let input = require('fs').readFileSync(filePath).toString().trim().split(" ").map((e)=>+e);
let max = Math.max(...input);
let index = input.indexOf(max);
input.splice(index, 1);
console.log(max + Math.max(...input))