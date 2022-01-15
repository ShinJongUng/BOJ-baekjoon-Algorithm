let inputs = require('fs').readFileSync('ans.txt').toString().trim().split('\n'); // /dev/stdin
inputs.sort();
let arr = {};
let ans = "";

for (let i = 1; i <= inputs[0]; i++) {
	if (arr[inputs[i][0]]) {
		arr[inputs[i][0]]++;
	} else {
		arr[inputs[i][0]] = 1;
	}
}

for (let i in arr) {
	if (arr[i] >= 5) 
        ans += i;
}

if(ans.length === 0){
    console.log('PREDAJA')
}
else{
    console.log(ans)
}