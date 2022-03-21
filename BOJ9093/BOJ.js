let [num, ...input] = require("fs").readFileSync("input.txt").toString().trim().split("\n");

for(let i = 0; i < num; i++){
    
    input[i] = input[i].split(" ");
    for(let j = 0; j < input[i].length; j++){
        input[i][j] = input[i][j].split('').reverse().join('');
    }
    console.log(input[i].join(' '))
}