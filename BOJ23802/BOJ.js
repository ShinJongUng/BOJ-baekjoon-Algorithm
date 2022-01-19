let inputs = require('fs').readFileSync('ans.txt').toString().trim(); // /dev/stdin

for(let i =1; i<= 5 * inputs; i++){
  for(let j =1; j<= 5 * inputs; j++){
    if(i <= inputs || j <= inputs){
      process.stdout.write('@')
    }
  }
  console.log()
}