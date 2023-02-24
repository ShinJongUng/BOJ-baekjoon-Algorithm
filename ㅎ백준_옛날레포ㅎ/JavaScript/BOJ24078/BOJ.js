const input = require('fs').readFileSync('ans.txt').toString().trim() // /dev/stdin

console.log(input % 21)