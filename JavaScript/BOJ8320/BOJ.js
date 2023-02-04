let input = require('fs').readFileSync('ans.txt').toString()// /dev/stdin
let square = 0

for(let i = 1; i<parseInt(input)+1; i++)
    for(let j = 1; j <= i; j++)
        if(i*j <= input)
            square++


console.log(square)