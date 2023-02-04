const fs = require('fs');
let [n, ...input] = fs.readFileSync("ans.txt").toString().trim().split("\n");

let total = 0, min = Number.MAX_SAFE_INTEGER, isFinish = false;
for(let i = 0; i < input.length; i++){
    input[i] = input[i].split(' ').map((e)=>parseInt(e))
}
input.sort((a,b)=>a[1] - b[1])

for(let x of input){
    total += x[0]
    min = Math.min(min, x[1] - total)
    if(x[1] < total)  isFinish = true;
}

if(isFinish) console.log(-1)
else console.log(min)