public class if_else {
  public static void main(String[] args) {
    
    
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
    
  }
}
    