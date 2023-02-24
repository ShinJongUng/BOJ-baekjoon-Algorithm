const filePath = process.platform === 'linux' ? '/dev/stdin' : './ans.txt';
let input = require('fs').readFileSync(filePath).toString().trim()
let num = Number(input)
let arr = new Array()
while(num != 0){
    arr.push(Math.abs(num % -2))
    num = Math.ceil(num / -2)
}
console.log(arr.length == 0 ? 0 : arr.reverse().join(''))