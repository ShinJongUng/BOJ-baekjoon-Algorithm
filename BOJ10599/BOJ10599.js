const fs = require('fs');
let n = fs.readFileSync("ans.txt").toString().trim().split("\n");

for(let i = 0;;  i++){
    n[i] = n[i].split(' ').map((e)=>parseInt(e))
    if(n[i][0] === 0 &&n[i][1] === 0&&n[i][2] === 0&& n[i][3] === 0){
        break;
    }
    console.log((n[i][2] - n[i][1]) + " " + (n[i][3] - n[i][0]))
}

