public class arrays {
  public static void main(String[] args) {
    
    
    // Java Arrays
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
      
  }
}
