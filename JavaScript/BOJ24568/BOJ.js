const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let input = require('fs').readFileSync(filePath).toString().trim().split("\n"), count = 99;
input = input[0]
inputs = parseInt(input)
if(inputs >= 100){
    for(let i = 100; i <= inputs; i++){
        let tempArr = [], sequence = 0, tempI = i.toString()
        tempArr = tempI.split("").map((e)=>+e)
        sequence =  tempArr[0] - tempArr[1]
        if(tempArr[1] - tempArr[2] == sequence){
            count++
        }
    }
    console.log(count)
}
else{
    console.log(inputs)
}
