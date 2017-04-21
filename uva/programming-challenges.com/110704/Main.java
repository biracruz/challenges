import java.util.*;
import java.io.*;
import java.lang.*;


/**
 * Created by biracruz on 23/12/2009.
 * Submission ID: 302710
 * Problem: Factovisors
 */

public class Main {

static List<Integer> factores = new ArrayList<Integer>();
static long a;
static long b;
static  BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

public static void main(String args[]) throws IOException{
   String line;
   int c=0;
   while((line  = reader.readLine())!=null){
            String cleanLine = line.trim().replaceAll("\\s+", " ");
            String[] tokens = cleanLine.split("\\s+");
            if (tokens.length == 2) {
                 a = new Long(tokens[0]).longValue();
                 b = new Long(tokens[1]).longValue();
                 if (a == 0 && b == 0)break;
               if(b!=0 ){
                   if(b == 1 || a > b ){
                       System.out.println(b+" divides "+a+"!");
                   }else{
                       if( prime_factors(b)&&fact_values(a) )
                        System.out.println(b+" divides "+a+"!");
                         else
                        System.out.println(b+" does not divide "+a+"!");
                   }
               }
               else{
                    System.out.println(b+" does not divide "+a+"!");
            }
            }
   }
   }

static boolean prime_factors(long n) {
        if(n==0){return false;}
        factores.clear();
    	long temp = n;
	if (n==1){factores.add(1);}
	while (true) {
		if (temp % 2 == 0) {
			temp = temp/2;
			factores.add(2);
		}
		else break;
	}
	int num = 3;
	while (temp > 1) {
		boolean flag = true;
		while (flag) {
			if (temp % num == 0) {
				temp = temp/num;
				factores.add(num);
			}
			else flag = false;
		}
		num = num + 2;
	}
        return true;
        }

static boolean  fact_values(long n){
    boolean removed;
    List<Integer> exc = new ArrayList<Integer>();//lista de fatores excluidos
    while(factores.size()>0){
        int num  = factores.get(0);
        int i=0 ;
        removed = false;
        for(i +=num;i<=a;i=i+num){// andando do primeiro multiplo de num até o ultimo <= a
            int pos = Collections.binarySearch(exc, i,null);
            if(pos<0){
                factores.remove(0);
                exc.add((pos*(-1))-1,i);
                removed = true;
                break;
            }
        }
        if(!removed) return false;
    }
    exc.clear();
    return true;
}
}