const level = 5;
let tree = "";
for(let i = 1; i<=level; i++){
    tree = "";
    for(let k = 0; k<level-i;k++){
        tree = tree + " ";
    }
    for(let j = 0; j<i*2-1;j++){
        tree = tree + "*";
    }

    console.log(tree);
}