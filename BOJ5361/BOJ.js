let input = require('fs').readFileSync('ans.txt').toString().split("\n") // /dev/stdin
let N = input[0], Arr = [350.34, 230.90, 190.55, 125.30, 180.90]
for(let i = 1; i<=N ; i++)
{
  let tempInput = input[i].split(' '),  sum = 0
  for(let j = 0; j<5; j++){
    sum += (parseInt(tempInput[j]) * Arr[j])
  }
  console.log(`$${sum.toFixed(2)}`)
}
