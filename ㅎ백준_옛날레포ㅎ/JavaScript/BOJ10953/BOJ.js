let inputs = require('fs').readFileSync('ans.txt').toString().trim().split('\n');// /dev/stdin

for(let i = 1; i <= inputs[0]; i++){
    let CommaSplit = inputs[i].split(',');
    console.log(parseInt(CommaSplit[0]) + parseInt(CommaSplit[1]))
}