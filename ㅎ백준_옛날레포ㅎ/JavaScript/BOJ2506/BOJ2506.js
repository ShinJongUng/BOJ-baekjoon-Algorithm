const fs = require('fs');
let [a, inputs] = fs.readFileSync("ans.txt").toString().trim().split("\n");
let answer = 0, cnt = 0;
a = parseInt(a);
inputs = inputs.split(" ");

for(let x of inputs){
    if(x === '1'){
        cnt++;
        answer += cnt;
    }
    else{
        cnt = 0;
    }
}

console.log(answer);
