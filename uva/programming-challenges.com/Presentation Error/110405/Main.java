import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Scanner;


/**
 * Created by biracruz on 26/12/2009.
 * Submission ID: 302858
 * Problem: Shoemaker's Problem  
 */


public class Main {
    static List<Task> p = new ArrayList<Task>();

    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        float a,b,c;
        int cases = sc.nextInt();
        String line;
        while(cases!=0){
            sc.nextLine();
            int lines = sc.nextInt();
            for(int i = 0;i<lines;i++){
                a= sc.nextFloat();
                b= sc.nextFloat();
                c= a/b;
                Task t = new Task(i, c);
                p.add(t);
            }
           Collections.sort(p);
        Iterator it = p.iterator();
        StringBuffer sb = new StringBuffer();
         sb.append(it.next());
        while(it.hasNext()){
            sb.append(" ");
            sb.append(it.next());
        }
         System.out.println(sb+"\n");
         p.clear();
            cases--;
        }
        
    }
    
    public static class Task  implements Comparable<Task> {
        public int index;
        public float p;

        public Task(int i , float p) {
            index = i+1;
            this.p = p;
        }

        public int compareTo(Task t) {
            if(this.p<=t.p)return -1;
            else return 1;
        }

        public String toString(){
            return Integer.toString(index);
        }
    }
}