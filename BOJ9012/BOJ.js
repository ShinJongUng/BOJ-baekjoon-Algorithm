let inputs = require('fs').readFileSync('ans.txt').toString().trim().split('\n'); // /dev/stdin

for(let i = 1; i <= parseInt(inputs[0]); i++){
    const stack = []
    let result = true
    for(let j = 0; j< inputs[i].length; j++){
        if(inputs[i][j] === '(')
            stack.push(inputs[i][j])
        else {
            if(!stack.pop()){
                result = false
            }
        }
    }
    if(stack.length !== 0){
        result = false
    }
        

    if(result == false)
        console.log('NO')
    else
        console.log('YES')
}