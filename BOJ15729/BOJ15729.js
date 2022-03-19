const fs = require('fs');
let [n, input] = fs.readFileSync("ans.txt").toString().trim().split("\n");


input = input.split(" ").map((e)=>parseInt(e));

let arr = Array.from({length:n}, ()=>1), cntArr = Array.from({length:n}, ()=>1);
let answer = 0;
for (let i = 0; i < n; i++) {
    if (cntArr[i] % 2 === 0 && arr[i] !== input[i] ) {
        for (let j = 0; j < 2; j++) {
            cntArr[i + j + 1]++;
        }
        answer++;
    }
    if (cntArr[i] % 2 !== 0 && arr[i] === input[i]) {
        for (let j = 0; j < 2; j++) {
            cntArr[i + j + 1]++;
        }
        answer++;
        }
    }
console.log(answer);