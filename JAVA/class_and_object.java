
// Java is associated with classes and objects
// Object is a member (also called an instance) of a Java class.
// Class is like an object constructor, or a "blueprint" for creating objects


class Calc{             // creating a class 'Calc'

    int num1;           // adding the variables/attributes
    int num2;   
    int result;

    public void perform(){          // adding the method     -- void is used as there is no return value
        result = num1 + num2;
    }

    // Constructor
        /*
            It is a Member Method (default)
            It has same name as class name
            It will never return aything
            It will be used to allocate the memory
        */
        
    public Calc(){                    // default constructor
        System.out.println("This is written in Constructor");
    }

    // constructor overloading
    // we can have multiple constructor but with diff Signature
    public Calc(int n){               
        num1 = n;
        num2 = n *2;
    }
    public Calc(double d){            
        num1 = (int) d;
        num2 = ((int) d) *5;
    }
}


public class class_and_object {
    public static void main(String[] args)
    {
        Calc myObj;                  // ref
        myObj = new Calc();          // creating an Object using the constructor -- 'Calc()'
        // myObj = new Calc(7.5);   

        // object knows something(variable) and does something(methods)
        // constuctor is called by default (automatically)


        myObj.num1 = 5;             // assigning the variables
        myObj.num2 = 8; 
        // System.out.println(myObj.num1);       // result from constructor
        // System.out.println(myObj.num2);       // result from constructor
        
        myObj.perform();            // calling the method
        System.out.println(myObj.result);       // result
    }


}
