const filePath = process.platform === 'linux' ? '/dev/stdin' : 'ans.txt';
const input = require('fs').readFileSync(filePath).toString().trim()
const ans = new Array();

for(let i = 0; i < input.length; i++){
    ans.push(input.slice(i, input.length));
}

console.log(ans.sort().join("\n"))