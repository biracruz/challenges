import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


/**
 * Created by biracruz on 29/05/2016.
 * Submission ID: 606996
 * Problem: The Knights Of The Round Table
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    //reference: http://mathworld.wolfram.com/Incircle.html
    // so, r = sqrt [ (s - a)(s - b)(s - c) / s ] where s = (a + b + c) / 2

    public static void main(String[] args) throws IOException {

        String line;
        while((line = br.readLine())!=null){
            String[] numbers =  line.split(" ");
            double a = Double.valueOf(numbers[0]);
            double b = Double.valueOf(numbers[1]);
            double c = Double.valueOf(numbers[2]);
            double s = (a + b + c)/2.0;
            double r = (a!= 0 && b != 0 && c!= 0)? Math.sqrt(((s-a)*(s-b)*(s-c))/s):0;
            System.out.printf("The radius of the round table is: %.3f\n", r);
        }
    }
}