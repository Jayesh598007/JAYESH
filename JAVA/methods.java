public class methods {

    // Java Methods    
    // method is a block of code which only runs when it is called
    // methods are used to perform certain actions( functions)
    // System.out.println()  -- is an example of java in-built method

    /*
        Syntax:
        public class Main {
            static void myMethod() {        -- // myMethod() is the name of method 
            // code to be executed
            }
        }
    */

    
    static int myLogic (int x , int y){         // dataType and methodName (parameters)
        int z;                                  // declare variable 
        z = (x>y)? (x - y) : (x + y);           // logic 
        return z;                               // return value
    }
    
    static void greet(String fName){                // fName is a Parameter
        System.out.println("Hello, " + fName);      // no return value
    }
    
    static void checkAge(int age){                  // method with logic
        if (age <18){
            System.out.println("You are under age");
        }
        else{
            System.out.println("You are an Adult");
        }
    }
    
    // method overloading
    static int plusMethod(int a, int b){
        return a + b;
    }

    static double plusMethod( double a1 , double b1){
        return a1 + b1;
    }

    public static void main(String[] args) {

        // Method example
        {
            int a = 5;
            int b = 2;
            int c = myLogic(a, b);
            System.out.println(c);
            
            int a1 = 5;
            int b1 = 7;
            int c1 = myLogic(a1, b1);
            System.out.println(c1);
            
            
            // Method invocation using object Creation
            /*
            methods obj = new methods();
            
            int a2 = 9;
            int b2 = 4;
            int c2 = obj.myLogic(a2, b2);
            System.out.println(c2);
            */
            
        }


        // Parameter
        {
            // Information can be passed to methods as 'parameter'
            // parameters can be single or multiple, accordingly
                
                
            greet("Jayesh");               // Jayesh is an Argument to method 'greet'
            greet("Kalpesh");              // kalpesh is an Argument to method 'greet'
        
            /*
            The void keyword, used in the examples above, indicates that the method should not return a value
            If you want the method to return a value,
            you can use a primitive data type (such as int, char, etc.) instead of void, and use the return keyword inside the method
            */


            checkAge(20);                   // 20 is a parameter to method checkAge
        }


        // Method Overloading
        {
            // with method overloading, multiple methods can have the same name with different parameters

            int myNum1 = plusMethod(5, 8);
            double myNum2 = plusMethod(4.5, 2.4);
            System.out.println("int: " + myNum1); 
            System.out.println("int: " + myNum2); 
        }


        // Java Scope
        {
            // variables are only accessible inside the region they are created. This is called 'scope'
                
                // code here CANNOT use x
                int x = 3;
                // code here CAN use x 
                System.out.println(x);
                


            //block of code refers to all of the code between curly braces {}
                   
                    // code here CANNOT use x
                {
                    // code here CANNOT use x
                    int x1 = 3;
                    // code here CAN use x 
                    System.out.println(x1);
                }
                    // code here CANNOT use x
        }
        


    }
}


