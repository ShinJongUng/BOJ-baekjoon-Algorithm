const fs = require('fs');
let [n, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
input = input.split(' ').map((e)=>parseInt(e))
input.sort((a,b)=>a-b)

let arrNum = Math.floor((n-1)/2)
console.log(input[arrNum])