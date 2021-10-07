// 13. Events in JS


function clicked(){         // this func will show below msg in console when the button is clicked
    // added to button
    document.querySelectorAll('.Box')[1].innerHTML = "<b> The button was clicked </b>";
    console.log("The button was Clicked");
}


/*
window.onload = function(){     //this function will show below msg in console when the page has been load
    console.log("the document is loaded");
}
firstContainer.addEventListener('click', function(){        // 'click' eventlistener on element (mouse click)
    console.log("click on Container");                      // events will be shown in console
})
click.addEventListener('mouseover', function(){        // 'mouseover' eventlistener on element (mouse hover)
    console.log("mouse on button");
})
click.addEventListener('mouseout', function(){        // 'mouseout' eventlistener on element (mouse hover)
    console.log("mouse out of button");
})
*/


let prevHTML = document.querySelectorAll('.Box')[1].innerHTML;
dom.addEventListener('mousedown', function(){        // 'mousedown' eventlistener on element (when click)
    document.querySelectorAll('.Box')[1].innerHTML = "<b> This is a BOLD Box </b>";
    console.log("mouse down when clicked on button");
})
dom.addEventListener('mouseup', function(){        // 'mouseup' eventlistener on element (when click released)
    document.querySelectorAll('.Box')[1].innerHTML = prevHTML;
    console.log("mouse up when clicked on button");
})

