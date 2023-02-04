const [A,B] = require('fs').readFileSync('ans.txt').toString().trim().split('\n') // /dev/stdin
let ans = parseInt(A) + parseInt(B)

while(ans > 12){
    ans -=12
}

console.log(ans)