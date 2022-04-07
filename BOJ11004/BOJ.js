const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let [input, inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");
input = input.split(' ').map((e)=>+e)
inputs = inputs.split(' ').map((e)=>+e).sort((a,b)=>a-b)
console.log(inputs[input[1]-1])