const fs = require('fs');
let [num, ...inputs] = fs.readFileSync("ans.txt").toString().trim().split('\n');
let arr = []
for(let i =0 ; i < num; i++){
    arr.push(inputs[i].split(' ').map((e)=>parseInt(e)))
}
arr = arr.sort((a,b)=>(b[1]) - (a[1]))
let temp = arr[0][1] - arr[0][0]

for(let i = 1; i < num; i++){
    if(arr[i][1] < temp){
        temp = arr[i][1] - arr[i][0]
    }
    else{
        temp -= arr[i][0]
    }
}

if(temp >= 0){
    console.log(temp)
}
else{
    console.log(-1)
}