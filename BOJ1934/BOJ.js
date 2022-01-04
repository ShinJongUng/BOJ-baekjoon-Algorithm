let inputs = require('fs').readFileSync('ans.txt').toString().trim().split('\n');// /dev/stdin

let Euclid = (x, y) =>{
    if (y === 0) 
        return x;
    else 
        return Euclid(y, x%y);
}

let  LCM = (x, y) =>(x*y) / Euclid(x,y);


for (let i = 1; i< inputs.length; i++){
    let  input = inputs[i].split(' ');
    console.log(LCM(input[0], input[1]))
}
