let [num, ...input] = require("fs").readFileSync("input.txt").toString().trim().split("\n");

let answer = 0
for(let i = 0; i < num; i++){
    let tempArr = [], tempWord = ''
    for(let j = 0; j <input[i].length; j++){
        if(tempWord != input[i][j]) {
            if(tempArr.includes(input[i][j]) > 0){
                answer -= 1;
                break;
            }
            else{
                tempArr.push(tempWord);
            }
        }
        tempWord = input[i][j]
    }
    answer++;
}

console.log(answer)