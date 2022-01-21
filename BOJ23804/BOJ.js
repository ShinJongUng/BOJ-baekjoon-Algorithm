let inputs = require('fs').readFileSync('ans.txt').toString().trim(); // /dev/stdin

for(let i =1; i<= 5 * inputs; i++){
  for(let j =1; j<= 5 * inputs; j++){
    if((1 <= i && i <= inputs) || j <= inputs || i >= 5 * inputs - inputs + 1){
      process.stdout.write('@')
    }
  }
  console.log()
}