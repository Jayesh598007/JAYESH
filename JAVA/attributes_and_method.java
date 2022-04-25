
class myFile{           // new class
    
    // attributes
    final int x = 8;        // attributes cannot be reassigned  -- 'final'
    int a =6; 


    // methods
    static void myMethod(){
        System.out.println("Hello Jayesh... Welcome to infosys");
    }

}

public class attributes_and_method {

    public static void main ( String[] args){
        myFile myObj1=  new myFile();       // object 1
        myFile myObj2=  new myFile();       // object 2

        myObj1.a = 25;          // accessing and modifying the attribute 'a'
        // myObj1.x = 25;          // this gives error as it cannot be assigned; coz -- 'final'

        System.out.println(myObj1.x);       // returns final/fixed value
        System.out.println(myObj1.a);       // returns changed value
        System.out.println(myObj2.a);       // returns default value

        myFile.myMethod();          // calling the method  -- it only perform when it is called

    }
    
}
