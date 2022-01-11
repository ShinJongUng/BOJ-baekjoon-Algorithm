let inputs = require('fs').readFileSync('ans.txt').toString().trim().split('\n'); // /dev/stdin

for(let i = 1; i<=inputs[0]; i++){
    for(let j = 0; j < inputs[i]; j++){
        for(let k = 0; k < inputs[i]; k++){
            if(j == 0 || k == 0 || j == inputs[i] - 1 || k == inputs[i] - 1)
                process.stdout.write('#')
            else
                process.stdout.write('J')
        }
        console.log();
    }
    console.log();
}