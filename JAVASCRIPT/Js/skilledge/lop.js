function colorDiff(){
    document.getElementById('circle').style.backgroundColor= 'salmon'
}




let courses = [
    "angular",
    [123, "jayesh"],
    "react",
    "v6",
];

// access data on specific position
let coursesClone = courses;
console.log(coursesClone[1][0])

console.log("*******************************");
console.log(courses)




// JSON Stringify and parse
arrjson = JSON.stringify(courses)  // tostring
console.log(arrjson)


console.log(JSON.parse(arrjson))  // to array

// normal to string and array function
arrStr = courses.toString()
console.log(arrStr)
console.log(Array(arrStr))

console.log("*******************************");




// new arrays
let dat1 = [1, 5, 3, 8, 4, 3456]
let dat3 = ["jayesh", "jay", "kartik", "light"];

// spread operator
let comb = [...dat1 , ...dat3, 10]
console.log(comb)

// rise operator
let [one, two, three, ...all] = comb
console.log(all)

// concatination
let concat = [dat1 + dat3]
console.log(concat)

let num = [2, 5, 3, 8,7, 1];

console.log(num.sort((a, b)=>
    {
        return b-a
    }
))

