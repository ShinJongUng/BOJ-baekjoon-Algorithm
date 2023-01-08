const filePath = process.platform === 'linux' ? '/dev/stdin' : 'ans.txt';
let [N, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");

class Stack{
    constructor(arr){
        this.arr = arr;
    }
    s_push(num){
        this.arr.push(num);
    }
    s_pop(){
        let data = this.arr.pop();
        if(!data) return -1
        return data;
    }
    s_empty(){
        if(this.arr.length > 0){
            return 0;
        }
        else{
            return 1;
        }
    }
    s_top(){
        if(!this.arr[this.arr.length - 1]) return -1;
        return(this.arr[this.arr.length - 1])
    }
    s_size(){
        return this.arr.length;
    }
}

const arr = [], ans = [];
let stack = new Stack(arr);
inputs.map((value)=>{
    value = value.trim().split(" ");

    if(value[0] == "push"){
      stack.s_push(parseInt(value[1]));
    }
    else if(value[0] == "top"){
        ans.push((stack.s_top()));
    }
    else if(value[0] == "size"){
        ans.push(stack.s_size());
    }
    else if(value[0] == "pop"){
       ans.push(stack.s_pop());
    }
    else if(value[0] == "empty"){
        ans.push(stack.s_empty());
    }
})

console.log(ans.join("\n"))