const fs = require('fs');
let [num, ...inputs] = fs.readFileSync("ans.txt").toString().trim().split('\n');
let countArr = Array.from({length:num}, ()=>1);
let firstArr = inputs[0].split(' ').map((e)=>parseInt(e))
let secondArr = inputs[1].split(' ').map((e)=>parseInt(e))

firstArr.sort((a,b)=>a-b)
secondArr.sort((a,b)=>b-a)

let sum = 0;
for(let i = 0; i < num; i++){
    sum += firstArr[i] * secondArr[i];
}

console.log(sum)