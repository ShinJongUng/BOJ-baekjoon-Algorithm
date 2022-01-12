let inputs = require('fs').readFileSync('ans.txt').toString().trim(); // /dev/stdin

let ans = 0;
for(let i = 1; i <=500; i++){
    for(let j = i; j<=500; j++){
        if(j * j === i * i + parseInt(inputs))
            ans++
    }
}

console.log(ans)