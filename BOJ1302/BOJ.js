let [n, ...input] = require('fs').readFileSync('input.txt').toString().split('\n')
let answer = [], arrCnt = [];

for(let i = 0; i < n; i++){
  if(answer.some((a)=> a == input[i]) == true){
    arrCnt[answer.indexOf(input[i])]++
  }
  else{
    answer.push(input[i])
    arrCnt.push(1)
  }
}

let maxindex = Math.max(...arrCnt)
answer = answer.filter((n, i)=>{ return arrCnt[i] == maxindex }).sort()

console.log(answer[0])