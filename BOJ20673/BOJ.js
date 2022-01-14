let inputs = require('fs').readFileSync('ans.txt').toString().trim().split('\n'); // /dev/stdin

if(inputs[0]<=50 && inputs[1]<=10){
    console.log("White")
}
else if(inputs[1]>30){
    console.log("Red")
}
else{
    console.log("Yellow")
}