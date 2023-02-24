const filePath = process.platform === 'linux' ? '/dev/stdin' : 'ans.txt';
const input = require('fs').readFileSync(filePath).toString().trim().split("\n");
let N = input[0], N_cards = input[1].split(" "), M = input[2], M_cards = input[3].split(" ");
let ansObj = new Object();
const ans = new Array();
for(let i = 0; i < N; i++){
    N_cards[i] = parseInt(N_cards[i])
    ansObj[N_cards[i]] ? ansObj[N_cards[i]]++ : ansObj[N_cards[i]] = 1;
}

for(let i = 0; i < M; i++){
    M_cards[i] = parseInt(M_cards[i]);
    ansObj[M_cards[i]] ? ans.push(ansObj[M_cards[i]]): ans.push(0);
}


console.log(ans.join(" "))