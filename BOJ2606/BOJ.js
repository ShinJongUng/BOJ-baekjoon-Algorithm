const filePath = process.platform === 'linux' ? '/dev/stdin' : '../ans.txt';
let [computer, node, ...inputs] = require('fs').readFileSync(filePath).toString().trim().split("\n");
let graph = new Array(parseInt(computer) + 1), ans_dfs = [], visited = new Array(parseInt(computer) + 1).fill(false)
for(let i = 0; i < graph.length; i++) {graph[i] = []}
for(let i = 0; i < parseInt(node); i++){
    let [index, element] = inputs[i].split(" ").map((e)=>+e)
    graph[index].push(element)
    graph[element].push(index)
}
DFS(1)
console.log(ans_dfs.length - 1)
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