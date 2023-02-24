const fs = require('fs');
let [num, ...inputs] = fs.readFileSync("ans.txt").toString().trim().split('\n');
let [stringCnt, brand] = num.split(' ').map((e)=>parseInt(e)) , answer = 0;

let brandArr = [], six_string_min = Number.MAX_SAFE_INTEGER, one_string_min= Number.MAX_SAFE_INTEGER;
for(let i = 0; i < brand; i++){
    brandArr[i] = inputs[i].split(' ').map((e)=>parseInt(e))
    if(six_string_min > brandArr[i][0]){
        six_string_min = brandArr[i][0]
    }
    if(one_string_min > brandArr[i][1]){
        one_string_min = brandArr[i][1]
    }
}


if(one_string_min * 6 > six_string_min){
    while(stringCnt>=6){
        answer+= six_string_min
        stringCnt -= 6
    }
    let tempAns = 0;
    while(stringCnt>=1){
        tempAns+= one_string_min
        stringCnt -= 1
    }
    if(tempAns > six_string_min){
        answer += six_string_min
        console.log(answer)
    }
    else{
        answer += tempAns
        console.log(answer)
    }
}
else{
    while(stringCnt>=1){
        answer+= one_string_min
        stringCnt -= 1
    }
    console.log(answer)
}
