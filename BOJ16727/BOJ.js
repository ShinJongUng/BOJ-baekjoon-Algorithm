const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
let F = input[0].split(' ').map((a)=>parseInt(a))
let S = input[1].split(' ').map((a)=>parseInt(a))
if(F[0]+S[1] === S[0]+F[1]){
    if(F[0] === S[0]){
        console.log('Penalty')
    }
    else if(F[0] > S[0]){
        console.log('Esteghlal')
    }
    else{
        console.log('Persepolis')
    }
}
else{
    if(F[0]+S[1] > S[0]+F[1]){
        console.log('Persepolis')
    }
    else{
        console.log('Esteghlal')
    }
}