const fs = require('fs');
let [num, inputs] = fs.readFileSync("ans.txt").toString().trim().split('\n');
inputs = inputs.split('')
const benchCnt = num.split(' ').map((e)=>parseInt(e))
let search = 0;

for(let j = 0; j < benchCnt[0]; j++){
    if(inputs[j] === 'P'){
        for(let i = Math.max(j - benchCnt[1], 0); i<=Math.min(j + benchCnt[1], benchCnt[0]); i++){
            if(inputs[i] === 'H'){
                inputs[i] = 0;
                search++;
                break;
            }
        }
    }
}


console.log(search)