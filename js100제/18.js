const score=['20','30','40'];

let sum = 0;

for(let i = 0; i<score.length;i++){
    sum = sum + parseInt(score[i], 10);
}

console.log(Math.floor(sum/score.length));