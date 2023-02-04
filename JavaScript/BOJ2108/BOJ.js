const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let [input, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n").map((e)=>+e);
inputs.sort((a,b)=>a - b)
let tempArr = [...inputs]
let sum = inputs.reduce((acc, v)=> acc + v, 0)
let temp = [], tempCnt = 0, tempBefore = -4001, tempMax = 1;
for(let i = 0; i < input; i++){
    if(tempBefore != inputs[i]){
        tempCnt = 1
        tempBefore = inputs[i]
    }
    else{
        tempCnt++
    }

    if(tempMax == tempCnt){
        temp.push(inputs[i])
    }
    if(tempMax < tempCnt){
        temp = []
        temp.push(inputs[i])
        tempMax = tempCnt
    }
}

let FAns = Math.round(sum / input)
if(FAns == -0){
    console.log(0)
}
else{
    console.log(FAns)
}
console.log(inputs[Math.floor(input/2)])
if(temp.length > 1){
    temp.sort((a,b)=>a-b)
    console.log(temp[1])
}
else{
    console.log(temp[0])
}
console.log(Math.max(...tempArr) - Math.min(...tempArr))