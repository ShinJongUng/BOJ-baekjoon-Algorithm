let inputs = require('fs').readFileSync('ans.txt').toString().trim(); // /dev/stdin

function a(n) {
    if (n == 0) 
		return 0
    else if (n == 1) 
		return 1
    else 
		return a(n-1) + a(n-2)
}
console.log(a(inputs))