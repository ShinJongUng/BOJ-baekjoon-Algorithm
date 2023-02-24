const fs = require('fs');
let inputs = fs.readFileSync("ans.txt").toString();
let answer = 0, input = 1000 - inputs;

while(input >= 500){
    input -= 500;
    answer++;
}
while(input >= 100){
    input -= 100;
    answer++;
    
}
while(input >= 50){
    input -= 50;
    answer++;
console.log(answer);

}
while(input >= 10){
    input -= 10;
    answer++;
}
while(input >= 5){
    input -= 5;
    answer++;
}
while(input >= 1){
    input -= 1;
    answer++;
}



console.log(answer);