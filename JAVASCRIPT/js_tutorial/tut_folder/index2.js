// 5. operators in JS

/*
// arithmatic operators 
var x = 8;
var y = 4;
console.log("the values of x + y is ", x+y)
console.log("the values of x / y is ", x/y)
console.log("the values of x - y is ", x-y)
console.log("the values of x * y is ", x*y)

// assignment operators 
var c = x;
console.log("The value of c is ",c)
c += 9;
console.log("the values of c+9 is ",c);
c -= 9;
console.log("the values of c-9 is ",c);
c *= 9;
console.log("the values of c*9 is ",c);
c /= 9;
console.log("the values of c/9 is ",c);

// comparison operators 
var j = 34;
var k = 67;
console.log(j==k);
console.log(j<=k);
console.log(j>=k);

// logical operators 
console.log(true && true);      // logical and 
console.log(true && false);     // and 
console.log(false && false);    // and 
console.log(false && true);     // and 
console.log(true || false);     // logical or 
console.log(true || true);      // or 
console.log(false || false);    // or 
console.log(false || true);     // or
console.log(!false);            // logical not
console.log(!true);             // logical not
*/




// 6. functions in JS

function avg(a, b) {
  return (a + b) / 2;
}
function sum(a, b) {
  return a + b;
}
function product(a, b, c) {
  return a * b * c;
}
// function is used/was made on basis of DRY principle - Do Not Repeat Yourself
// thus we can make multiple functions of various task and can use only after calling it to perform the specific task
// functions can be used only if it is called, as shown below
c1 = avg(34, 62);
c2 = avg(5, 61);
console.log(c1, c2);

// Arrow function 
/*
function summ(s, t){
  return(s + t);
}
*/  // the above function can also be written as below arrow function

summ = (s, t)=>{
  return (s+t);
}
