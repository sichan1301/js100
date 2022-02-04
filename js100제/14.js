// 3의 배수면 짝 아니면 그대로 출력

const n = prompt();

if(n%3==0 && n!=0){
    console.log("짝!");
}
else{
    console.log(n);
}