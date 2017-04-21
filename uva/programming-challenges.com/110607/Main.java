import java.util.*;
import java.io.*;
import java.lang.*;


/**
 * Created by biracruz on 15/12/2009.
 * Submission ID: 302205
 * Problem: Selfdescribing Sequence
 */

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static List<Integer> list = new ArrayList<Integer>();
    static     List<Integer> s = new ArrayList<Integer>();
    static  int maxnumber  = 2000000000;

    public static void main(String args[]) throws IOException{
        gen();
        int n, UpIndex;
        while ((n = Integer.parseInt(br.readLine().trim()))!= 0){
            if(( UpIndex = Collections.binarySearch(list, n, null))>=0){
                s.add( UpIndex+1);
            } else{
                UpIndex*=-1;
                s.add(UpIndex-1);
            }
        }

        Iterator it = s.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }
    }

    static void gen(){
         list.add(0,1); list.add(1,2); list.add(2,4);
         for(int i = 1;list.get(list.get(i)-1)<maxnumber ; i++){
            for(int j = list.get(i);j<list.get(i+1);j++){
                list.add(j, list.get(j-1)+i+1);
            }
        }
    }
    
}