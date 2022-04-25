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

  }
}   