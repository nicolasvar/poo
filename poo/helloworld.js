class helloworld{
    constructor(){
        this.name = "";
    }
    sayHello(){
        return "Hello, World ${this.name}!";
    }
}
const object1 = new helloworld();
object1.name = "Nicolas";
console.log(object1.sayHello());