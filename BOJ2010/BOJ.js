let input = require('fs').readFileSync('/dev/stdin').toString().split("\n") // /dev/stdin
let N = parseInt(input[0])
let PlugNum = 1
for(let i = 1; i<=N ; i++)
{
    let MultiPlug = parseInt(input[i])
    PlugNum += (MultiPlug-1)
}
console.log(PlugNum)
