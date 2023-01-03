const filePath = process.platform === 'linux' ? '/dev/stdin' : 'ans.txt';
const [, inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");
let ans = new Set();

inputs.split(" ").map((value)=>{
    ans.has(value) ? ()=>{} : ans.add(value); 
})

console.log(Array.from(ans).sort((a, b)=> a-b).join(" "));
