const filePath = process.platform === 'linux' ? '/dev/stdin' : './ans.txt';
let input = require('fs').readFileSync(filePath).toString().trim().split("\n").join('');
let s =""
for(let i = 0; i < input.length; i++){
    if(input[i] == input[i].toUpperCase()){
        s += input[i].toLowerCase()
    }
    else{
        s+= input[i].toUpperCase()
    }
}
console.log(s)