const fs = require('fs');
let [n, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
input = input.split(" ").map((e)=>parseInt(e));
let sum1 = 0, sum2 = 0;

for(let x of input){
    sum1 += Math.floor(x / 2)
    sum2 += x % 2
}

if((sum1 - sum2)%3 == 0 && sum1 >= sum2){
    console.log("YES")
}
else{
    console.log("NO")
}