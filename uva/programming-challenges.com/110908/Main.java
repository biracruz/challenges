import java.util.Scanner;


/**
 * Created by biracruz on 27/05/2016.
 * Submission ID: 606738
 * Problem: Hanoi Tower Troubles Again!  
 */


public class Main {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int testCases = sc.nextInt();
        while (testCases != 0){
            boolean inserting = true;
            int newNumber = 1;
            int numberOfPegs = sc.nextInt();
            int[] lastPegs = new int[numberOfPegs];
            for(int i = 0; i < numberOfPegs; i++){
                lastPegs[i] = 0;
            }
            while(inserting){
                int n = newNumber;
                for(int i = 0; i < numberOfPegs; i++){
                    int lastNumber = lastPegs[i];
                    if (TestSquare(lastNumber, newNumber)){
                        lastPegs[i] = newNumber;
                        newNumber = newNumber + 1;
                        i = -1;
                    }
                }
                if(n == newNumber) //not possible to insert
                    inserting = false;
            }
            System.out.println(newNumber-1);
            testCases--;
        }
    }

    public static boolean TestSquare(int a, int b){
        if(Math.sqrt(a+b) % 1 == 0 || a == 0)
            return true;
        else
            return false;
    }

}