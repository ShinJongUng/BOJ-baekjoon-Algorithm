const filePath = process.platform === 'linux' ? '/dev/stdin' : './ans.txt';
let [first, second] = require('fs').readFileSync(filePath).toString().trim().split(' ')
let min = first.length;
for (let i=0; i<=second.length-first.length; i++) {
    let current = 0;
    for (let j=i; j<i+first.length; j++) {
        if (first[j-i] !== second[j]) {
            current++
        }
    }
    min = current < min ? current:min;
}
console.log(min);