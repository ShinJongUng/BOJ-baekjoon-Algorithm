const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let [input, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");
let [n, m, v] = input.split(" ").map((e)=>+e)
let graph = new Array(n+1), visited = new Array(n+1).fill(false)
for(let i = 0; i < graph.length; i++) graph[i] = []
for(let i = 0; i < m; i++){
    let [index, element] = inputs[i].split(" ").map((e)=>+e)
    graph[index].push(element)
    graph[element].push(index)
}
graph.forEach(e => {e.sort((a,b)=>a-b)})
let ans_dfs = [], ans_bfs = []
DFS(v)
console.log(ans_dfs.join(" "))
visited.fill(false)
BFS(v)
console.log(ans_bfs.join(" "))

function DFS(v){
    if(visited[v] == true) return
    ans_dfs.push(v)
    visited[v] = true
    for(let i = 0 ; i < graph[v].length; i++){
        if(visited[graph[v][i]] == false){
            DFS(graph[v][i])
        }
    }
}
function BFS(v){
    let Queue = [v]
    while(Queue.length){
        let temp = Queue.shift()
        if(visited[temp] == true) continue
        visited[temp] = true
        ans_bfs.push(temp)
        for(let i = 0; i < graph[temp].length; i++){
            if(visited[graph[temp][i]] == false){
                Queue.push(graph[temp][i])
            }
        }
    } 
}