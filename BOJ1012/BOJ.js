const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let [N, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");
let ansArr = [], tempObj = {}
inputs.split(" ").map((e)=>+e)
let set = Array.from(new Set([...inputs])).sort((a,b)=>a-b)
set.forEach((element, index)=>Object[element] = index)
for(let i = 0 ; i < N; i++){
    ansArr.push(Object[inputs[i]])
}
console.log(ansArr.join(" "))