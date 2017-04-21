import java.lang.*;
import java.util.*;
import java.io.*;


/**
 * Created by biracruz on 11/12/2009.
 * Submission ID: 301821
 * Problem: Where's Waldorf?  
 */


public class Main {

    static int cases;
    static final int PMAX = 20;
    static final int COLMAX = 50;
    static char t[][];
    static int numberWords;
    static String p[];
    static int m, n;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String args[]) throws IOException {
        String REGEX_WHITESPACE = "\\s+";

        cases = Integer.parseInt(br.readLine().trim());
        while (cases > 0) {
            br.readLine();
            String cleanLine = br.readLine().trim().replaceAll(REGEX_WHITESPACE, " ");
            String[] tokens = cleanLine.split(REGEX_WHITESPACE);
            if (tokens.length == 2) {
                m = new Integer(tokens[0]).intValue();
                n = new Integer(tokens[1]).intValue();
                if (n > COLMAX) {
                    throw new RuntimeException("Number of columns exceded");
                }
            } else {
                throw new RuntimeException("Wrong input");
            }
            read_text();
            if ((numberWords = Integer.parseInt(br.readLine().trim())) > PMAX) {
                throw new RuntimeException("Number of words exceded");
            }
            read_words();
            int positions[][] = new int[numberWords][2];
            positions = search_p(positions);
            for (int e = 0; e < numberWords; e++) {
                if (positions[e][0] != 0 && positions[e][1] != 0) {
                    System.out.println(positions[e][0] + " " + positions[e][1]);
                }
            }
            cases--;

                
            
        }
    }

    static void read_text() {
        try {
            t = new char[m][n];
            char c;
            int i = 0;
            while (i < m) {
                int j = 0;
                while (true) {
                    c = Character.toLowerCase((char) (br.read()));
                    if (c == '\n') {
                        break;
                    }
                    if (c != ' ') {
                        t[i][j] = c;
                        j++;
                    }
                }
                i++;
            }
        } catch (IOException e) {
            System.out.println("IOException Error!\n");
        }

    }

    static void read_words() {
        p = new String[numberWords];
        try {
            for (int i = 0; i < numberWords; i++) {
                p[i] = br.readLine().trim().toLowerCase();
            }
        } catch (IOException e) {
            System.out.println("IOException Error!\n");
        }
    }

    static int[][] search_p(int positions[][]) {

        boolean found[] = new boolean[PMAX];
        int v[] = {0, - 1, - 1, -1, 0, 1, 1, 1};
        int h[] = {-1, -1, 0, 1, 1, 1, 0, -1};

        for (int l = 0; l < m; l++) {
            for (int c = 0; c < n; c++) {
                for (int w = 0; w < numberWords; w++) {                      
                    if (p[w].charAt(0) != t[l][c] || found[w] ) { continue;}//se a primeira letra já é diferente procure outra palavra
                    for (int d = 0; d < 8; d++) {
                           int i = 1;
                           int x = l;
                           int y = c;
                            while(i <  p[w].length()){
                                 if((x += v[d]) < 0 || (y += h[d]) < 0 ){break;}
                                 if(x == m || y == n){break;}
                                 if(p[w].charAt(i) != t[x][y]){break;}
                                 i++;
                            }
                            if(i == p[w].length()){
                                positions[w][0] = l+1;
                                positions[w][1] = c+1;
                                found[w] = true;
                                break;
                            }  
                   }
                }
            }
        }
        return positions;
    }
}