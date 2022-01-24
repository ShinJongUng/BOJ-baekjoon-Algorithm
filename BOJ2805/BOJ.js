const [f_input,s_input] = require('fs').readFileSync('ans.txt').toString().trim().split("\n"); // /dev/stdin

const N = f_input.split(" ")[1]
const trees =[]
let max = Math.max
s_input.split(" ").forEach(s_func=>{
    s_func = +s_func
    if(+s_func>max) {
        max=s_func
    }
    trees.push(s_func)
})

let min = 0
let ans = 0
while(min<=max){
    let mid = parseInt((min+max)/2);
    let cnt =0;
    trees.forEach(tree=>{
    let garbage = tree-mid
    if(garbage>0) 
        cnt+=garbage
    })
    if(cnt>=N){
        if(mid>ans){
            ans=mid
        }
        min=mid+1
    }
    else{
        max=mid-1
    }
}

console.log(ans)