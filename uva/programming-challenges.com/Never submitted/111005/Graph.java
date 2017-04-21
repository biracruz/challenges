import java.util.*;

public class Graph
{
    static final int MAXV = 10000;

    //HELP FROM http://opendatastructures.org/ods-java/12_2_AdjacencyLists_Graph_a.html
    public Map<Integer, ArrayList<Node>> adj;
    public int nvertices;

    public class Node{
        private int adj;
        private int relationCode;
        public Node(int adj, int relationCode){
            this.adj = adj;
            this.relationCode = relationCode;
        }

    }
    public enum RelationEnum {
        FRIEND(1), ENEMY(0), UNKNOWN(-1), UNDETERMINED(-100);

        private final int code;

        private RelationEnum(int code){
            this.code = code;
        }

        public int getCode(){
            return code;
        }
    }

    Graph(int n)
    {
        nvertices = n;
        adj = new HashMap<Integer, ArrayList<Node>>();
        for(int i = 0; i <= nvertices; i++){
            adj.put(i, new ArrayList<Node>());
        }
    }

    void ReadGraph()
    {
        int x,y, r;
        Scanner sc = new Scanner(System.in);
        nvertices = sc.nextInt();
        for(int i=1;i<=nvertices;i++)
        {
            x=sc.nextInt();
            y=sc.nextInt();
            r= sc.nextInt();
            InsertEdge(x,y,r);
        }
    }
    private boolean hasEdge(int i, int j) {

        for (Node n :adj.get(i)) {
            if (n.adj == j){
                return true;
            }
        }
        return false;
    }

    int getEdgeRelation(int i, int j){
        if (hasEdge(i, j)){
            return adj.get(i).get(j).relationCode;
        }else{
            return RelationEnum.UNDETERMINED.getCode();
        }
    }
    void InsertEdge(int x, int y, int relationCode)
    {
        int previousCode = getEdgeRelation(x,y);
        if(previousCode == RelationEnum.UNDETERMINED.getCode()){

            adj.get(x).add(new Node(y, relationCode));
        }else{
            if(relationCode != previousCode){
                adj.get(x).remove(y);
                adj.get(x).add(new Node(y, RelationEnum.UNKNOWN.getCode()));
            }
        }
    }

    void PrintGraph()
    {
        for(int i=0;i<nvertices;i++)
        {
            ArrayList<Node> list = adj.get(i);
            for(int j=0; j<list.size();j++){
                System.out.printf(" %d",list.get(j).relationCode);
            }
            System.out.printf("\n");
        }
    }
}