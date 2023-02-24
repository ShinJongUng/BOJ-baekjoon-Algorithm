let inputs = require('fs').readFileSync('ans.txt').toString().trim(); // /dev/stdin

for(let i =5 * inputs; i>=1; i--){
  for(let j =5 * inputs; j>=1 ; j--){
    if(i <= inputs || j <= inputs){
      process.stdout.write('@')
    }
  }
  console.log()
}