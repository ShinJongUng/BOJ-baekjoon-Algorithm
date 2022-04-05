const input = require('fs').readFileSync('../ans.txt').toString().trim().split("\n"); // /dev/stdin
let f_input = input[0].split(" ").map((e)=>Number(e))
let f_output = f_input[0] * 6 + f_input[1] * 3 + f_input[2] * 2 + f_input[3] + f_input[4] * 2

let s_input = input[1].split(" ").map((e)=>Number(e))
let s_output = s_input[0] * 6 + s_input[1] * 3 + s_input[2] * 2 + s_input[3] + s_input[4] * 2

console.log(f_output + " " + s_output)