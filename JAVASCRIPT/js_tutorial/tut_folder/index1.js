// javascript


// 1. ways to print in JS
console.log("Hello World!");
// alert("your password is in small characters");
// document.write("This is a Pink Document");


// 2. JS console API
// console.log("Hello World!", 4+34, "another log");
// console.warn("this is a warning");
// console.error("this is an error");


// 3. JS variables
// variables are the containers to store the data values
var number1 = 34;
var number2 = 12;
console.log(number1 + number2);


// 4. Datatyes in JS
/*
At a very high level there are two types of datatypes 
1. Primitive datatypes: undefined, booleans, str, number, null, symbol
2. Referance datatypes: arrays and objects
*/

// number
var number1 = 34;

// string
var str1 = "this is a string";
var str2 = "this is also a string";

// booleans
var a = true;
var b = false;
console.log(a, b);

// null and undefined
var und;        // this is bydefault undefined
var n = null;   // this is null(void)
console.log(und);
console.log(n);

// object
var marks = {
  ravi: 34,
  jayesh: 98,
  kartik: 78,
};
console.log(marks);

// array
var arr = [1, 2, 3, "Hello", 5, 6, 7];
console.log(arr);


// 'var' , 'let' and 'const' all are used for variable declaration 
var aa = 34;    // it is used for global scope (defined throughout program)
let ab = 436;   // it is a block scoped (defined for specific function)
const ac = 0;   // it is used to define variable which cannot be changed(immutable)


