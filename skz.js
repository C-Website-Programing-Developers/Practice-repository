const name = 'John'
const age = 30;
const rating = 4.5;
const isCool = true;
const x = null;
const y = undefined;
let z;

console.log("My name is " +name+ " and I am " +age);
console.log(`My name is ${name} and I am ${age}`);


const s = 'Hello world!';

console.log(s.substring(0,5).toUpperCase());


const s = 'technology, computers, it, code'

console.log(s.split(', '))


const fruits = ["apples", "oranges", "pears", 10, true];

fruits[3] = "grapes";

fruits.push("mangos");

fruits.unshift("strawberries");

fruits.pop();

console.log(Array.isArray(fruits));

console.log(fruits.indexOf("oranges"));

console.log(fruits);


const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    hobbies: ["music","ball","sports"],
    address:{
        street:"50 main st",
        city:"Boston",
        state:"MA"
    }
}

person.email = "2012604@mail.nankai.edu.cn";

console.log(person);

const todos = [
    {
    id:1,
    text:"take me in.",
    isCompleted:true
    },
    {
    id:2,
    text:"take me out.",
    isCompleted:false,
    },
    {
    id:3,
    text:"take me no.",
    isCompleted:false,
    },
];

const todoJSON = JSON.stringify(todos);
console.log(todoJSON);


for(let i = 0; i<= todos.length; i++){
    console.log(todos[i].text);
}

for(let todo of todos){
    console.log(todo.text);
}

let i = 0;
while(i < 10){
    console.log(`While Loop Number: ${i}`);

    i++;
}

todos.forEach(function(todo)
{
    console.log(todos.text);
});

const todoText = todos.map(function(todo){
    return todo.text;
});

console.log(todoText);

const todoCompleted = todos.filter(function(todo){
    return todo.isCompleted === true;
});

console.log(todoCompleted);


const todoCompleted = todos.filter(function(todo){
    return todo.isCompleted === false;
}).map(function(todos){
    return todos.text;
})

console.log(todoCompleted);


const x = '10';

if(x == 10){
    console.log('x is 10.');
}


const x = '10';
const y = 27;

if(x === 10 || y > 20){
    console.log('x is 10.');
}
else if(x >= 10 && y >20){
    console.log('x is greater than 10.')
}
else{
    console.log('x is less than 10.')
}


const x = 10;

const color = x > 10 ? 'red' : 'blue';

console.log(color);

function addNums( num1 = 1, num2 = 1){
    return num1 + num2;
}

console.log(addNums(5,5));

const addNums = (num1 = 1, num2 = 1) =>  num1 + num2;

console.log(addNums(5,5));


const addNums = num1  =>  num1 + 5;

console.log(addNums(1));

todos.forEach((todo) => console.log(todo));

function Person(firstName,lastName,dob){
    this.firstName = firstName;
    this.lastName = lastName;
    this.dob = new Date(dob);
    this.getFullName = function(){
        return `${this.firstName} ${this.lastName}`;
    }
    this.getBirthYear = function(){
        return this.dob.getFullYear();
    }
}

const person1 = new Person('John','Doe','2002-1-7');
const person2 = new Person('Mary','Smith','1-7-2002');

console.log(person1.getBirthYear());


function Person(firstName, lastName, dob){
    this.firstName = firstName;
    this.lastName = lastName;
    this.dob = new Date(dob);
}

Person.prototype.getBirthYear = function(){
    return this.dob.getFullYear();
}

Person.prototype.getFullname = function(){
    return `${this.firstName} ${this.lastName}`;
}

class Person{
    constructor(firstName, lastName, dob){
        this.firstName = firstName;
        this.lastName = lastName;
        this.dob = new Date(dob);
    }

    getBirthYear(){
        return this.dob.getFullYear();
    }

    getFullname(){
        return `${this.firstName} ${this.lastName}`;
    }

}

const person2 = new Person('John','Doe','July 21, 1983');

console.log(person2);

const form = document.getElementById('my-form');

console.log(form);

const items = document.querySelectorAll('.item');

items.forEach((items) => console.log(items));

const ul = document.querySelector('.items');

ul.firstElementChild.textContent = 'Hello';
ul.children[1].innerText = 'Brad';
ul.lastElementChild.innerHTML = '<h1>Hello</h1>';

const btn = document.querySelector('.btn');
btn.getElementsByClassName.background = "color:red";

const btn = document.querySelector('.btn');

btn.addEventListener('click',(e) => {
    e.preventDefault();
    document.querySelector('#my-form').style.background = '#ccc';
    document.querySelector('body').classList.add('bg-dark');
    document.querySelector('.items').lastElementChild.innerHTML = '<h1>Hello</h1>';
});

btn.addEventListener('mouseout',(e) => {
    e.preventDefault();
    document.querySelector('#my-form').style.background = '#ccc';
    document.querySelector('body').classList.add('bg-dark');
    document.querySelector('.items').lastElementChild.innerHTML = '<h1>Hello</h1>';
});

const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('#users');

myForm.addEventListener('submit',onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if(nameInput.value === '' || emailInput === ''){
        msg.classList.add('error');
        msg.innerHTML = 'Please enter all fields.';

        setTimeout(() => msg.remove(), 3000);
    }
    else{
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(`${nameInput.value} : ${emailInput.value}`));
        userList.appendChild(li);

        nameInput.value = '';
        emailInput.value = '';
    }
}

const place = "world";
const greeting = "Hello";

console.log(`${greeting},${place}`);
