import java.util.Scanner;


/**
 * Created by biracruz on 29/05/2016.
 * Submission ID: 606909
 * Problem: Unidirectional TSP  
 */


public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (sc.hasNextInt()) {

            int rows = sc.nextInt();
            int columns = sc.nextInt();
            int[][] M = new int[rows][columns];

            //read matrix
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < columns; j++) {
                    M[i][j] = sc.nextInt();
                }
            }

            //from the end of the matrix calculate the weights
            for(int j = columns - 2; j >= 0; j--) {

                int[] actualColumn = new int[rows];
                int[] nextColumn = new int[rows];

                //read columns
                for (int i = 0; i < rows; i++) {
                    actualColumn[i] = M[i][j];
                    nextColumn[i] = M[i][j + 1];
                }

                int[] newColumn = CalculateWeightColumn(actualColumn, nextColumn);
                //substitute column on matrix
                for (int i = 0; i < rows; i++) {
                    M[i][j] = newColumn[i];
                }
            }

            //from the begin of the matrix choose the path
            int[] path = new int[columns];
            //first column
            int firstValue = M[0][0];
            for (int i = 0; i < rows; i++) {
                if (M[i][0] < firstValue) {
                    firstValue = M[i][0];
                    path[0] = i;
                }
            }


            for(int j= 1; j < columns; j++){
                int[] col = new int[rows];
                for (int i = 0; i < rows; i++) {
                    col[i] = M[i][j];
                }
                path[j] = ChooseNextMove(path[j-1],col)[0];

            }

            int totalWeight = 0;
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < columns; j++){

                sb.append(path[j]+1);
                sb.append(" ");
                //calculate path weight
                if(j+1 < columns){
                    totalWeight = totalWeight + M[path[j]][j] - M[path[j+1]][j+1];
                }else{
                    totalWeight = totalWeight + M[path[j]][j];
                }
            }
            sb.deleteCharAt(sb.length()-1);
            System.out.println(sb.toString());
            System.out.println(totalWeight);
        }
    }

    private static int[] CalculateWeightColumn(int[] colA, int[] colB) {
        int[] newColumn = new int[colA.length];
        for (int i = 0; i < colA.length; i++) {
            int lowest = ChooseNextMove(i, colB)[1];
            newColumn[i] = colA[i] + lowest;
        }
        return newColumn;
    }

    //[0] = line index
    //[1] = line weight
    private static int[] ChooseNextMove(int lineIndex, int[] col){

        // up        /  []
        // same [] ->   []
        // down      \  []
        int upIndex = (col.length + lineIndex - 1) % col.length;
        //lineIndex
        int downIndex = (col.length + lineIndex + 1) % col.length;
        int up = col[upIndex];
        int same = col[lineIndex];
        int down = col[downIndex];
        int[] lowest = new int[2];

        lowest[0] = upIndex;
        lowest[1] = up;

        if(same < lowest[1] || ( same == lowest[1]  && lineIndex < lowest[0])){
            lowest[0] = lineIndex;
            lowest[1] = same;
        }

        if(down < lowest[1] || ( down == lowest[1]  && downIndex < lowest[0])){
            lowest[0] = downIndex;
            lowest[1] = down;
        }
        return lowest;
    }
}
