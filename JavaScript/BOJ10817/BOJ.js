let inputs = require('fs').readFileSync('ans.txt').toString().trim().split(' '); // /dev/stdin

let a = parseInt(inputs[0]), b = parseInt(inputs[1]), c = parseInt(inputs[2])


if(a > b){
    if(a > c){
        if(b> c){
            console.log(b)
        }
        else{
            console.log(c)
        }
    }
    else{
        console.log(a)
    }    
}
else{
    if(b > c){
        if(a>c){
            console.log(a)
        }
        else{
            console.log(c)
        }
    }
    else{
        console.log(b)
    }
}