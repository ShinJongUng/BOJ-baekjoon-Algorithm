const fs = require('fs');
let [n, inputs] = fs.readFileSync("ans.txt").toString().trim().split("\n");
let input = inputs.split(" ").map((e)=>parseInt(e))
n = parseInt(n);
let speed = input[n-1];

for(let i = n - 2; i>=0; i--){
    speed = Math.ceil(speed / input[i]) * input[i]
}
console.log(speed)