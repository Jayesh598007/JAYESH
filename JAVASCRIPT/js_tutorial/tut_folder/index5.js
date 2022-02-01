// 12. DOM Manipulation 
// Document Object Model -- DOM


/*
let elem = document.getElementById("click");
console.log(elem);

let pac = document.getElementsByClassName('Box');
console.log(pac);
pac[0].style.background = "yellow";       // style elemeny using JS
pac[0].classList.add("text-changed");     // adding new classes to elements using JS
pac[1].classList.add("bg-primary");       // change properties and elements using JS
console.log(pac[0].innerHTML);            // it returns the data within the element
console.log(pac[0].innerText);            // it returns the text in the element
tn = document.getElementsByTagName("div");        // it returns the element with the tag name ( div, span, h1, button, etc)
console.log(tn);

createdElement = document.createElement("p");       // created a new element
createdElement.innerText= "This is a created paragraph";      // inner text of the new element
tn[0].appendChild(createdElement);                  // add new element at last 

createdElement2= document.createElement("b");         // created a new element
createdElement2.innerText= "This is a created bold staement";     // inner text of the new element
tn[0].replaceChild(createdElement2, createdElement);              //replace new element with previous one 

tn[0].removeChild(createdElement2);         // to remove the element
// document.URL 
// document.scripts
// document.title
// document.location
// document.links
// document.images
// document.forms
// document.domain
*/

// Selecting using query 
let sel = document.querySelector('.Box');       // it returns the first element that matches the specified selectors
console.log(sel);
// let sel2 = document.querySelectorAll('.Box');  // it returns all element that matches the specified selectors
// console.log(sel2);


