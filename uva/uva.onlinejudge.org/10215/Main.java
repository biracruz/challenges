import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Locale;
import java.util.Scanner;


/**
 * Created by biracruz on 30/05/2016.
 * Submission ID: 17440504
 * Problem: The Largest/Smallest Box ...
 */


public class Main {
    //reference: http://www.ufrgs.br/espmat/disciplinas/funcoes_modelagem/modulo_IV/complementos4c.htm
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException {

        String line;
        final  double EPSILON = 0.0000001;;
        while((line = br.readLine())!= null){
            String[] numbers =  line.split(" ");
            double l = Double.valueOf(numbers[0]);
            double w = Double.valueOf(numbers[1]);
            if(l <= 0 || w <= 0){
                System.out.printf(Locale.US,"%.3f %.3f %.3f\n", 0f, 0f, 0f);
            }else{
                //V = x * ( l - 2x) * (w -2x)
                //V' = 12x^2 - 4x*(l+w)+l*w, when V' = 0, then V = max.
                double a = 12.0;
                double b = -(4.0 * l + 4.0 * w);
                double c = l * w;
                double delta = b * b - 4.0*a*c;
                double max = (- b - Math.sqrt(delta ))/(2.0*a);
                //double max = (w+l-Math.sqrt(w*w-w*l+l*l))/6;
                double min = Math.min(l,w)/2.0;
                System.out.printf(Locale.US,"%.3f %.3f %.3f\n", max+EPSILON, 0f, min+EPSILON);
            }

        }
    }
}