class Wizard{
    constructor(a,b,c){
        this.health = a;
        this.mana = b;
        this.armor = c;
    }
    attack(){
        console.log("파이어볼");
    }
}

const x = new Wizard(545, 210, 10);

console.log(x.health, x.mana, x.armor);

x.attack();

// 출력
// 545 210 10
// 파이어볼