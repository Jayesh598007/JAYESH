
//  14.SetTimeout and Setinterval in JS
logKaro = ()=>{                 // function
    document.querySelectorAll(".Box")[1].innerHTML = "<b> Login </b>"
    console.log("login complete");
}

setTimeout(logKaro, 2000);          // it allows us to run a function once after the interval of time      
//--------(function, time(ms))
// setInterval(logKaro, 3000);         // it allows us to run a function repeatedly
// use 'clearInterval/clearTimeout' to cancel 'setInterval/setTimeout' 



// 15. Local Storage in JS 

localStorage.setItem("name", "jayesh");        // to set localStorage 
console.log(localStorage.getItem("name"));     // to get the name in LocalStorage
console.log(localStorage);                     // to check the localStorage name
// localStorage.removeItem("name");            // to remove the item
// localStorage.clear();                       // to clear all storage

