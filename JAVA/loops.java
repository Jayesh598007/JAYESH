public class loops {
  public static void main(String[] args){

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
  }
   
}
