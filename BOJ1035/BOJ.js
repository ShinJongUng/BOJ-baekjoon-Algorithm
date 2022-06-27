const filePath = process.platform === 'linux' ? '/dev/stdin' : './ans.txt';
let [input, ...inputs] = require('fs').readFileSync(filePath).toString().split('\n').map((e)=>parseInt(e))
const dp = new Array(input).fill(0)

dp[0] = inputs[0];
dp[1] = inputs[0] + inputs[1];
dp[2] = Math.max(inputs[0] + inputs[2], inputs[1] + inputs[2]);
for(let i = 3; i < input; i++){
    dp[i] = Math.max(inputs[i] + inputs[i - 1] + dp[i - 3] , dp[i - 2] +  inputs[i]);
}
console.log(dp[input - 1]);