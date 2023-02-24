const filePath = process.platform === 'linux' ? '/dev/stdin' : 'ans.txt';
let input = require('fs').readFileSync(filePath).toString().trim().split("\n");

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
}


const arr = [...new Array(parseInt(input))].map((_, i) => i + 1);
const ans = [];
let queue = new Queue(arr);


for(;;){
    ans.push(queue.s_pop()); //젤 위 카드 삭제
    if(queue.s_size() == 0) break;
    queue.s_push(queue.s_pop()); //젤 위 카드 아래로 내리기
}

console.log(ans.join(" "));