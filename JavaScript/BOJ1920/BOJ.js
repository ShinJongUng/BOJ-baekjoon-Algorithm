const fs = require('fs');
let input = fs.readFileSync('input.txt').toString().split('\n')

let N = input[1].split(' ').map((e)=>parseInt(e)).sort((a,b)=>a-b)
let M = input[3].split(' ').map((e)=>parseInt(e))

const binarySearch = (list, target, left, right, mid) => {
    mid = Math.floor((left + right) / 2);

  if (right < left) {
    return list[mid] == target ? 1 : 0;
  }

  if (list[mid] > target) {
    right = mid - 1;
  } else {
    left = mid + 1;
  }

  return binarySearch(list, target, left, right, mid);
  }


console.log((M.map(m => binarySearch(N, m, 0, N.length-1, 0))).join('\n'))
