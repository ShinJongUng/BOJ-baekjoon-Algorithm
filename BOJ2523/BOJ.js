let inputs = require('fs').readFileSync('/dev/stdin').toString().trim();// /dev/stdin
for(let i = 1; i <= inputs; i++){
    for(let j = 1; j<= i; j++){
        process.stdout.write('*');
    }
    console.log();
}

for(let i = inputs - 1; i >=1; i--){
    for(let j = 1; j<= i; j++){
        process.stdout.write('*');
    }
    console.log();
}
