import java.util.Scanner;

/**
 * Created by biracruz on 23/12/2009.
 * Submission ID: 307149
 * Problem: Little Bishops 
 */

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean stop = false;
        while (!stop) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            if (n == 0 & k == 0) {
                stop = true;
            }else{
                if(!(n == 0 && k == 0))
                System.out.println(bishops(n, k));
            }
        }
        }

     static long bishops(int n, int k)
{
    if(n==0)return 0;
    long d1[] = new long[9];
    long d2[] = new long[9];

    /*  Determinando o número de células da diagonal-1 e d-2(branca ou preta):
    * d1 recebe os numeros impares em ordem crescente e repetidos(pela simentria
    * do tabuleiro). ex: n=4 ,d1={1,1,3,3}*/
    for (int i = 1; i <= n; ++i) {
        d1[i] = i % 2 != 0 ? i : d1[i - 1];
    }
    for (int i = 1; i <= n - 1; ++i) {
        d2[i] = i % 2 != 0 ? i + 1 : d2[i - 1];
    }

    /*c1 e c2 representam o numero de casos possiveis para por
    *j bispos na i-esima diagonal*/
    long c1[][] = new long[9][65];
    long c2[][] = new long[9][65];

    //casos basicos da recorrencia:0 bispos = 1, 0 diagonal = 0;
    for (int i = 0; i <= n; ++i) { c1[i][0] = 1;}
    for (int j = 1; j <= k; ++j) { c1[0][j] = 0;}
    for (int i = 0; i <= n - 1; ++i) { c2[i][0] = 1;}
    for (int j = 1; j <= k; ++j) { c2[0][j] = 0;}


    /*   Recorrencia:  Ex: n=3,k=2
     * c[3][2]=c[2][2]+c[2][1]=3
     * c[2][2]=c[1][2]+c[1][1]=2
     * c[2][1]=c[2][0]=1
     */
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k && j <= i; ++j) {
            c1[i][j] = c1[i - 1][j] + c1[i - 1][j - 1] * (d1[i] - j + 1);
        }
    }
    for (int i = 1; i <= n - 1; ++i) {
        for (int j = 1; j <= k && j <= i; ++j) {
            c2[i][j] = c2[i - 1][j] + c2[i - 1][j - 1] * (d2[i] - j + 1);
        }
    }

    long r = 0;
    for (int i = 0; i <= k; ++i) {
        r += c1[n][i] * c2[n - 1][k - i];
    }
    return r;
}
    }