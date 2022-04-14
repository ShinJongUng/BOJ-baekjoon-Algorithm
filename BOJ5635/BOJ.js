const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let [input, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");
inputs = inputs.map((e) =>e.split(" ").map((a,i)=>i!=0?parseInt(a):a))
for(let i = 0; i < parseInt(input)-1; i++){
    let min = i;
    for(let j = i + 1; j<input; j++){
        if(inputs[j][3] > inputs[min][3]){
            min = j
        }
        else if(inputs[j][3] == inputs[min][3] && inputs[j][2] > inputs[min][2]){
            min = j
        }
        else if(inputs[j][2] == inputs[min][2] && inputs[j][1] > inputs[min][1]){
            min = j
        }
        if(min !== i){
            [inputs[i], inputs[min]] = [inputs[min], inputs[i]]
        }
    }
}
console.log(inputs[0][0]);
console.log(inputs[parseInt(input-1)][0])