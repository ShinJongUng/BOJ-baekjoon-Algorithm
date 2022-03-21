let input = require("fs").readFileSync("input.txt").toString().trim().split("");
const compareArr = [ 'U', 'C', 'P', 'C'];
let compareCnt = 0;

for(let x of input){
    if(x === compareArr[compareCnt]) compareCnt++;
}

console.log(compareCnt >= 4 ? 'I love UCPC': 'I hate UCPC')