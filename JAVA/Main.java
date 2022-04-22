public class Main {

  // main() method is required and any code inside the main() method will be executed
  // "System" is a Java In-built class with containe useful methods such as "out" - which means output.
  // "curly braces {}" marks the beginning and the end of a block of code.

  public static void main(String[] args) {
    
    // Basic Intro
    {
      // println() method to print a line of text to the screen [[ preferrable ]]
      System.out.println("Jayesh Chaudhari is BACK!!!");
      System.out.println("Hello World");
      System.out.println("I am an Employee of Infosys");
      
      
      // print() method, which is similar to println() but it does not insert a new line at the end of the output
      System.out.print("This is first line and ");
      System.out.print("this is second line ");
      System.out.print("but both are merged as a single line");
      
      
      // Single-line comments start with two forward slashes (//)
      // Multi-line comments start with /* and ends with */
      System.out.println("we can also add a comment after a code");  // like this comment
    }
    
    // Variables 
    {
      // Variables are containers for storing data values
      /* 
      Syntax:
            type variableName = value;
      

      Types :
      String -  stores text, such as "Hello". String values are surrounded by double quotes
      int -     stores integers (whole numbers), without decimals, such as 123 or -123
      float -   stores floating point numbers, with decimals, such as 19.99 or -19.99
      char -    stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
      boolean - stores values with two states: true or false
      
      // Data Types
      Primitive:
        int myNum = 5;               // Integer (whole number)
        float myFloatNum = 5.99f;    // Floating point number
        char myLetter = 'D';         // Character
        boolean myBool = true;       // Boolean
        String myText = "Hello";     // String

        Non-primitive:
        strings, Classes, and Arrays
      */
        
      // String
      String fName = "Jayesh";
      System.out.println(fName);      // results Jayesh
      

      // int
      int myNum = 59;
      System.out.println(myNum);      // results 59

      int newNum;
      newNum = 235;
      System.out.println(newNum);     // results 235
      newNum = 876;
      System.out.println(newNum);     // results 876

      // use the final keyword (this will declare the variable as "constant", thus it is unchangable)
      final int newNum2 = 567;
      System.out.println(newNum2);    // results 567


      // float or double
      float deciOne = 23.56f;
      System.out.println(deciOne);
      double deciTwo = 3.76d;
      System.out.println(deciTwo);


      // boolean 
      boolean isJavaFun = true;
      System.out.println((isJavaFun)); 


      // char
      char myGrade = 'B';
      System.out.println(myGrade);
    }

    // println()
    {
      //println() is also used for displaying combining variables
      String firstName = "Jayesh ";
      String lastName = "Chaudhari";
      String fullName = firstName + lastName;
      System.out.println("My name is " + fullName); 

      int x = 5;
      int y = 6;
      int sum = x + y;
      System.out.println(sum);        // results sum as 11
      

      // declare multiple variables
      int a = 235, b = 34, c = 2325;
      int newSum = a + b + c;
      System.out.println(newSum);

      
      /*
      Identifiers
      variables must be identified with unique names
      Names can contain letters, digits, underscores, and dollar signs
      */
    }

    // TypeCasting 
    {
      // Type casting is when you assign a value of one primitive data type to another type.
      /*
        Widening Casting (automatically) - converting a smaller type to a larger type size
        byte -> short -> char -> int -> long -> float -> double

        Narrowing Casting (manually) - converting a larger type to a smaller size type
        double -> float -> long -> int -> char -> short -> byte      
      */


      // Widening casting 
      int intNine = 9;
      double newNine = intNine;

      System.out.println(intNine);       // results 9
      System.out.println(newNine);    // results 9.0


      // Narrowing casting
      double dubEight = 8;
      int intEight = (int) dubEight;

      System.out.println(dubEight);   // results 8.0
      System.out.println(intEight);   // results 8
    }

    // Operators 
    {
      // Operators are used to perform operations on variables and values.
      /*
        Types of operators:
          Arithmetic operators
            ( +   -   /   *   %   ++   --  )

          Assignment operators
            ( =   +=   -=   *=   /=  )

          Comparison operators
            ( ==   >   <   <=   >=  !=  )

          Logical operators
            ( ["and"- &&]  ["or"- ||]   ["not" - !]   )

          Bitwise operators
      */
    }

    // Java Strings
    {
      // java Strings - used for storing texts
      String name = "Jayesh";
      String greet = "Hello";


      // concatenation
      System.out.println(greet + " " + name);                        // results 'Hello Jayesh'
      System.out.println(greet.concat(" ").concat(name));       // results 'Hello Jayesh'
    
      System.out.println(greet.length());           // results the length of the variable
      System.out.println(name.toUpperCase());       // results JAYESH
      System.out.println(name.toLowerCase());       // results jayesh

      String txt = "find locate in this text.";
      System.out.println(txt.indexOf("locate"));    // results index of a character


      // Escape character
      // backslash (\) escape character turns special characters into string characters
      String quote = "Today is a \"Good\" day";    
      System.out.println(quote);

      // \n id for new line
      String newLine = "My name is Jayesh \nI work for infosys.";
      System.out.println(newLine);      // above text is printed in two diff lines
    }

    // Java Maths
    {
      // java Maths - allows you to perform mathematical tasks
      System.out.println(Math.max(25, 12));     // results max value
      System.out.println(Math.min(25, 12));     // results min value
      System.out.println(Math.abs(-4.7));             // results positive value

      System.out.println(Math.random());             // gives random number betn 0.0 and 1.0
      int randomNum = (int) (Math.random() * 101);
      System.out.println(randomNum);                 // gives random number betn 0 to 100
    }

    // Java booleans
    {
      // java Booleans
      boolean isJavaFun = true;
      boolean isFishTasty = false;
      System.out.println(isJavaFun);     // Outputs true
      System.out.println(isFishTasty);   // Outputs false


      int num1 = 10;
      int num2 = 9;
      System.out.println(num1<num2);      // returns false
      System.out.println(num1 == num2);      // returns false
    }

    // Java If.. Else
    {
      // if statement -- to specify a block of Java code to be executed if a condition is 'true'
      // else if statement -- to specify a new condition if the first condition is 'false'
      // else statement -- to specify a block of code to be executed if the condition is 'false'
      /*
        Syntax:
          if (condition1) {
            // block of code to be executed if condition1 is true
          } else if (condition2) {
            // block of code to be executed if the condition1 is false and condition2 is true
          } else {
            // block of code to be executed if the condition1 is false and condition2 is false
          }
      */
      int time = 22;
      if (time < 10) {
        System.out.println("Good Morning");
      }
      else if(time < 14){
        System.out.println("Good Day");
      }
      else{
        System.out.println("Good Afternoon");
      }


      // Shorthand if.. else..
      /*
        Syntax:
          variable = (condition) ? expressionTrue :  expressionFalse;
      */
      int num1 = 20;
      String result = (num1 < 18)? "Good day" : "Good evening";
      System.out.println(result);


      // java Switch 
      // switch statement -- to select one of many code blocks to be executed
      /*
        Syntax:
          switch(expression) {
            case x:
              // code block
              break;
            case y:
              // code block
              break;
            default:
              // code block
          }
     */
      int day = 4;
      switch (day) {
        case 4:
          System.out.println("Today is Thursday");
          break;              // break statement can also be used to jump out of a loop
        case 6:
          System.out.println("Today is Saturday");
          break;
        case 7:
          System.out.println("Today is Sunday");
          break;
        default:
          System.out.println("Looking forward to the Weekend");
        // Outputs "Looking forward to the Weekend"
      }
    }

    // Java while loop
    {
      // while loop -- loops through a block of code as long as a specified condition is 'true'
      /*
        Syntax:
          while(condition){
            // java code to be executed
          } 
      */
      int i = 0;
      while(i < 6){
        System.out.println(i);        // results i
        i++;                          // adds i every time 
      }


      // do-while loop -- execute the code block once, before checking if the condition is true,
      //  then it will repeat the loop as long as the condition is true.
      /*
        Syntax:
          do{
            // java code to be executed
          }
          while(condition)
      */
      int j = 0;
      do {
        System.out.println(j);
        j++;
      }
      while(j<4);
    }

    // Java for loop
    {
      // for loop -- When you know exactly how many times you want to loop through a block of code
      /*
        Syntax:
          for (statement 1; statement 2; statement 3) {
            // code block to be executed
          }

        statement 1 -- init
        statement 2 -- condition
        statement 3 -- increment
      */
      
      for (int a = 0; a<10; a++){
        System.out.println(a);
      }


      // for-each loop --  is used exclusively to loop through elements in an array
      /*
        Syntax:
          for (type varaibleName: arrayName) {
            // block of code to be executed
          }
      */

      String[] cars = {"volvo", "ford", "tata", "hyundai"};
      for (String i :cars){
        System.out.println(i);
      }
    }

    // Java break/continue statement
    {
      // java break  -- statement can also be used to jump out of a loop
      for (int j = 0; j<10; j++){
        if(j ==4){
          break;          // loop breaks at the condition
        }
        System.out.println(j);
      }
    
      // java continue -- breaks one iteration and continues with the next iteration in loop
      for (int k =0; k<10; k++){
        if (k==4){
          continue;       // loop skips the given condition
        }
        System.out.println(k);
      }
    }

    // Jsava Arrays
    {
      // Arrays are used to store multiple values in a single variable
      String[] cars = {"ford", "volvo", "mahindra", "lexus"};
      System.out.println(cars[2]);

      int [] myNum = { 3, 67, 234, 32};
      System.out.println(myNum[0]);

      cars[0] = "TATA";                     // changing the array element
      System.out.println(cars[0]);          
      System.out.println(cars.length);      // returns the arrays length


      // loop through an array 
      for(int i = 0; i < cars.length; i++){
        System.out.println(i);         // displays each array element using for loop
      }

      for (String i : cars){
        System.out.println(i);         // displays each array element using for loop
      }


      // java multidimensional array -- is an array of arrays.
      // to access the elements of the myNumbers array, specify two indexes
      int[][] myNumbers = {{2, 4, 3}, {8, 6, 9, 1}};
      System.out.println(myNumbers[1][2]);      // results the element[2] of array[1] 
    }

    // Java Methods
    {
      // method is a block of code which only runs when it is called
      // methods are used to perform certain actions( functions)


    }









    {
      // These notes are mfgd by:
      // Jayesh Chaudhari - 8380884059
      // jayeshchau598007@gmail.com
      // Thanks to w3schools.com
    }

  }
}   