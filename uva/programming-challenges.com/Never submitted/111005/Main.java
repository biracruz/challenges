/**
 * Created by BIRACRUZ on 27/05/2016.
 * Submission ID: 
 * Problem: War
 */

public class Main {
    public static void main(String[] args){
        Graph G = new Graph(3);
        G.InsertEdge(1,1, Graph.RelationEnum.ENEMY.getCode());
        G.InsertEdge(1,2, Graph.RelationEnum.FRIEND.getCode());
        G.InsertEdge(1,3, Graph.RelationEnum.FRIEND.getCode());
        G.InsertEdge(2,1, Graph.RelationEnum.FRIEND.getCode());
        G.InsertEdge(2,3, Graph.RelationEnum.FRIEND.getCode());
        G.PrintGraph();
    }
}