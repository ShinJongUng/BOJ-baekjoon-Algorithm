let [num, ...input] = require("fs").readFileSync("input.txt").toString().trim().split('\n');
for(let i =0; i < num; i++){
    input[i] = input[i].split(' ').map((e)=>parseInt(e))
}

for(let i =1; i < num; i++){
    input[i][0] += Math.min(input[i-1][1], input[i-1][2])
    input[i][1] += Math.min(input[i-1][0], input[i-1][2])
    input[i][2] += Math.min(input[i-1][0], input[i-1][1])
}
console.log((Math.min(...input[num-1])))