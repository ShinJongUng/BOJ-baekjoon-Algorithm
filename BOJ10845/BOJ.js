const filePath = process.platform === 'linux' ? '/dev/stdin' : 'ans.txt';
let [N, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");

class Queue{
    constructor(arr){
        this.arr = arr;
    }
    s_push(num){
        this.arr.push(num);
    }
    s_pop(){
        let data = this.arr.shift();
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
    s_size(){
        return this.arr.length;
    }
    s_front(){
        let data = this.arr[0];
        if(!data) return -1;
        else return data;
    }
    s_back(){
        let data = this.arr[this.arr.length - 1];
        if(!data) return -1;
        else return data;
    }
}


const arr = [], ans = [];
let queue = new Queue(arr);
inputs.map((value)=>{
    value = value.trim().split(" ");

    if(value[0] == "push"){
        queue.s_push(parseInt(value[1]));
    }
    else if(value[0] == "empty"){
        ans.push((queue.s_empty()));
    }
    else if(value[0] == "size"){
        ans.push(queue.s_size());
    }
    else if(value[0] == "pop"){
       ans.push(queue.s_pop());
    }
    else if(value[0] == "front"){
        ans.push(queue.s_front());
    }
    else if(value[0] == "back"){
        ans.push(queue.s_back());
    }
})

console.log(ans.join("\n"))