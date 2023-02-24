const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let [input, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");
let [n, m] = input.split(" ").map((e)=>+ e)
let graph = [], visited = Array.from(Array(n), () => new Array(m).fill(0));


for(let i = 0; i < n; i++) graph[i] = inputs[i].split("").map((e)=>+e)
BFS(0,0)
console.log(visited[n-1][m-1])

function BFS(y, x){
    let dx = [0,1,0,-1], dy = [1,0,-1,0]
    let Queue = []
    Queue.push({y : y, x : x})
    visited[y][x] = 1;

    while(Queue.length){
        let {y, x} = Queue.shift()
        for(let i = 0; i < 4; i++){
            let ax = x + dx[i], ay = y + dy[i]
            if(ax >= 0 && ay >= 0 && ax < m && ay < n){
                if(visited[ay][ax] == 0 && graph[ay][ax] == 1){
                    visited[ay][ax] = visited[y][x] + 1
                    Queue.push({y: ay, x: ax})
                }
            }
        }
    } 
}